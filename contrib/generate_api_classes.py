#!/usr/bin/python3


import os
import re
import sys
import textwrap
from xml.etree import ElementTree as ET

DIR = os.path.abspath(os.path.dirname(__file__))
OBS_DIR = os.path.join(DIR, "open-build-service")


if not os.path.exists(OBS_DIR):
    print(f"ERROR: The Open Build Service checkout doesn't exist: {OBS_DIR}", file=sys.stderr)
    print("Run the following commands first:", file=sys.stderr)
    print(f"  cd {DIR}", file=sys.stderr)
    print("  git clone https://github.com/openSUSE/open-build-service.git", file=sys.stderr)
    sys.exit(1)


# this removes the "ns0:" prefix from the SchemaParser.to_string() output
ET.register_namespace("", "http://relaxng.org/ns/structure/1.0")


class SchemaParser:
    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.root = None

    def to_string(self):
        ET.indent(self.root)
        return ET.tostring(self.root, encoding="utf-8").decode("utf-8")

    @staticmethod
    def ln(node):
        """
        Return local name (name without a namespace) of the ``node``.
        """
        return node.tag.split("}")[-1]

    def _parse(self, path):
        """
        Parse XML in given ``path``, return the root element.
        """
        doc = ET.parse(path)
        root = doc.getroot()
        return root

    def _expand_includes(self, node):
        """
        Replace includes with the content of the referenced schemas.
        """
        if self.ln(node) == "include":
            href = node.get("href")
            path = os.path.join(os.path.dirname(self.path), href)
            root = self._parse(path)
            self._expand_includes(root)
            return root[:]

        new_nodes = []
        for child in node:
            nodes = self._expand_includes(child)
            if nodes is None:
                continue
            if not isinstance(nodes, list):
                nodes = [nodes]
            new_nodes.extend(nodes)
        node[:] = new_nodes

        return node

    def _simplify(self, node, parent=None):
        """
        Simplify the schema by squashing some elements into attributes of related nodes.
        For example:
          <optional><element name="foo" /></optional>
          becomes
          <element name="foo" optional="1" />
        """
        ln = self.ln(node)

        node.attrib.pop("ns", None)

        # in each iteration an element goes in and is replaced with what's returned from _simplify()
        # - None -> remove
        # - node -> keep
        # - [nodes] -> replace with the list of nodes
        new_nodes = []
        for child in node:
            nodes = self._simplify(child, parent=node)
            if nodes is None:
                continue
            if not isinstance(nodes, list):
                nodes = [nodes]
            new_nodes.extend(nodes)
        node[:] = new_nodes

        if ln == "start":
            # remove <start>
            return None
        elif ln == "interleave":
            # replace <interleave> with its child nodes in the parent
            return node[:]
        elif ln == "optional":
            # replace <optional> with its child nodes in the parent
            for child_node in node:
                child_node.attrib["optional"] = "1"
            return node[:]
        elif ln == "oneOrMore":
            # replace <oneOrMore> with its child nodes in the parent
            for child_node in node:
                child_node.attrib["list"] = "1+"
            return node[:]
        elif ln == "zeroOrMore":
            # replace <zeroOrMore> with its child nodes in the parent
            for child_node in node:
                child_node.attrib["list"] = "0+"
            return node[:]
        elif ln == "text":
            # remove the <text> node
            return None
        elif ln == "data":
            # remove the <data> node
            return None
        elif ln == "documentation":
            # move <documentation> text to parent's "doc" attribute
            lines = node.text.splitlines()

            # remove leading empty lines
            while lines and not lines[0].strip():
                lines.pop(0)

            # remove trailing empty lines
            while lines and not lines[-1].strip():
                lines.pop(-1)

            doc = "\n".join(lines)
            doc = textwrap.dedent(doc)
            parent.attrib["doc"] = doc
            return None
        elif ln == "empty":
            # remove <empty />
            return None

        return node

    def _handle_children(self, node, result):
        for child in node:
            ln = self.ln(child)
            handler = getattr(self, f"handle_{ln}")
            handler(child, result, parent_name=self.ln(node))

    def _assert_node_name(self, node, name):
        ln = self.ln(node)
        assert ln == name, f"Invalid node name '{ln}'. Expected '{name}'"

    def _assert_empty_attrib(self, attrib):
        assert not attrib, f"There are unprocessed attributes left: {attrib}"

    def _assert_no_children(self, node):
        assert len(node) == 0, f"There are unexpected child nodes: {node[:]}"

    def _get_attrib(self, node):
        attrs = dict(node.attrib)

        # name is used as a key and doesn't belong to values, let's remove it
        attrs.pop("name", None)

        data = {
            "optional": attrs.pop("optional", None),
            "doc": attrs.pop("doc", None),
            "list": attrs.pop("list", None),
        }
        self._assert_empty_attrib(attrs)

        # remove those items from have value equal to None
        for k, v in list(data.items()):
            if v is None:
                del data[k]

        return data

    def handle_define(self, node, result, parent_name=None):
        self._assert_node_name(node, "define")
        attrs = dict(node.attrib)
        name = attrs.pop("name", None)
        self._assert_empty_attrib(attrs)

        define_data = {}
        self._handle_children(node, define_data)

        result.setdefault("defines", {})
        result["defines"][name] = define_data

    def handle_choice(self, node, result, parent_name=None):
        self._assert_node_name(node, "choice")

        data = self._get_attrib(node)
        self._handle_children(node, data)
        result["choices"] = data

    def handle_value(self, node, result, parent_name=None):
        """
        Create ``result["values"] = []`` and append ``node.text`` to it.
        """
        self._assert_node_name(node, "value")
        self._assert_no_children(node)
        self._assert_empty_attrib(node.attrib)

        result.setdefault("values", [])
        result["values"].append(node.text)

    def handle_element(self, node, result, parent_name=None):
        self._assert_node_name(node, "element")

        attrs = dict(node.attrib)
        name = attrs.pop("name", None)
        data = self._get_attrib(node)

        self._handle_children(node, data)

        elem = {name: data}
        if parent_name == "define":
            result.update(elem)
        else:
            result.setdefault("elements", {})
            result["elements"].update(elem)

    def handle_attribute(self, node, result, parent_name=None):
        self._assert_node_name(node, "attribute")

        attrs = dict(node.attrib)
        name = attrs.pop("name", None)
        data = self._get_attrib(node)

        self._handle_children(node, data)

        result.setdefault("attributes", {})
        result["attributes"][name] = data

    def handle_ref(self, node, result, parent_name=None):
        self._assert_node_name(node, "ref")
        result["ref"] = node.attrib["name"]

    def parse(self):
        self.root = self._parse(self.path)
        assert self.ln(self.root) == "grammar"

        self._expand_includes(self.root)
        self._simplify(self.root)

        result = {}
        self._handle_children(self.root, result)
        return result


def get_property_name(name, plural=False):
    name = name.replace("-", "_")
    if plural:
        if name.endswith("y"):
            name = name[:-1]
            name = f"{name}ies"
        else:
            name = f"{name}s"
    return name


def get_wrapper_module_and_class(ref):
    if not ref:
        return None, None

    wrapper_module = None
    wrapper_class = ref
    wrapper_class = re.sub("-element$", "", wrapper_class)
    wrapper_class = "".join(i.capitalize() for i in wrapper_class.split("-"))
    wrapper_class = wrapper_class or None

    if wrapper_class:
        wrapper_module = ref
        wrapper_module = re.sub("-element$", "", wrapper_module)
        wrapper_module = wrapper_module.replace("-", "_")

    return wrapper_module, wrapper_class


def parsed_schema_to_class(parsed_schema, define_name, class_name):
    definition = parsed_schema["defines"][define_name]

    # HACK
    if len(definition) != 1:
        return ""
    assert len(definition) == 1, f"{define_name} {class_name} {definition.keys()}"

    print("DEF", define_name, class_name, definition)

    if list(definition.keys()) == ["choices"]:
        pass
    else:
        definition = list(definition.values())[0]
#    print("DEF2", define_name, class_name, definition)

    result = []
    result += ["from typing import List"]
    result += ["from typing import Type"]
    result += [""]
    result += ["from . import _base"]

    imports = set()
    for name, data in definition.get("elements", {}).items():
        if "choices" in data:
            continue
        ref = data.get("ref", None)
        if not ref:
            continue
        wrapper_module, wrapper_class = get_wrapper_module_and_class(ref)
        imports.add(f"from .{wrapper_module} import {wrapper_class}")
    imports = sorted(imports)
    result += imports

    result += [""]
    result += [""]
    result += [f"class {class_name}(_base.ApiEndPointBase):"]

    attributes = list(definition.get("attributes", {}))
    elements = list(definition.get("elements", {}))
#    choices = definition.get("choices", "")
#    choices = choices.split(",") if choices else []
    choices = ""

    if any((attributes, elements, choices)):
        result += [""]
    if attributes:
        result += [f"    _attributes: List[str] = {attributes}"]
    if elements:
        result += [f"    _elements: List[str] = {elements}"]
    if choices:
        result += [f"    _choices: List[str] = {choices}"]

    for name, data in definition.get("attributes", {}).items():
        property_name = get_property_name(name, plural=False)
        if property_name == name:
            property_name_kw = ""
        else:
            property_name_kw = f", property_name=\"{property_name}\""

        doc = data.get("doc", None)
        if doc and not doc.strip():
            doc = None

        optional = bool(int(data.get("optional", "0")))

        choices = data.get("choices", "")
#        choices = choices.split(",") if choices else []

        if doc and choices:
            doc += "\n\n"
            doc += "Choices:\n"
            for choice in choices:
                doc += f"  - ``{choice}``\n"

        if doc:
            doc = textwrap.indent(doc, "        ")

        if any((optional, choices)):
            result += [""]
        if optional:
            result += [f"    _{property_name}_is_optional: bool = {optional}"]
        if choices:
            result += [f"    _{property_name}_choices: List[str] = {choices}"]

        result += [""]
        result += [f"    @property"]
        result += [f"    def {property_name}(self) -> str:"]
        if doc:
            result += [f'        """']
            for line in doc.splitlines():
                result += [line]
            result += [f'        """']
        result += [f"        return self._get_attribute(\"{name}\"{property_name_kw})"]
        result += [""]
        result += [f"    @{property_name}.setter"]
        result += [f"    def {property_name}(self, value: str):"]
        result += [f"        self._set_attribute(\"{name}\", value{property_name_kw})"]
        result += [""]
        result += [f"    @{property_name}.deleter"]
        result += [f"    def {property_name}(self):"]
        result += [f"        self._delete_attribute(\"{name}\"{property_name_kw})"]

    for name, data in definition.get("elements", {}).items():
        is_list = "list" in data

        doc = data.get("doc", None)
        if doc and not doc.strip():
            doc = None
        if doc:
            doc = textwrap.indent(doc, "        ")

        property_name = get_property_name(name, plural=is_list)
        if property_name == name:
            property_name_kw = ""
        else:
            property_name_kw = f", property_name=\"{property_name}\""

#        print(name, data)
        optional = bool(int(data.get("optional", "0")))

        choices = data.get("choices", "")
#        choices = choices.split(",") if choices else []

        if choices:
            # no need to wrap choices in a wrapper class
            # TODO: fix
            wrapper_class = None
        else:
            wrapper_class = data.get("ref", "")
            wrapper_class = re.sub("-element$", "", wrapper_class)
            wrapper_class = "".join(i.capitalize() for i in wrapper_class.split("-"))
            wrapper_class = wrapper_class or None
            if wrapper_class:
                wrapper_module = data.get("ref", "")
                wrapper_module = re.sub("-element$", "", wrapper_module)
                wrapper_module = wrapper_module.replace("-", "_")

        if wrapper_class and is_list:
            pytype = f"List[{wrapper_class}]"
        elif wrapper_class:
            pytype = f"{wrapper_class}"
        elif is_list:
            pytype = "List[str]"
        else:
            pytype = "str"

        attributes = list(data.get("attributes", {}))
        elements = list(data.get("elements", {}))

        result += [f"# {data}"]
        if any((is_list, wrapper_class, optional, choices, attributes, elements)):
            result += [""]
        if is_list:
            result += [f"    _{property_name}_is_list: bool = True"]
        if wrapper_class:
#            result += [f"    from .{wrapper_module} import {wrapper_class}"]
            result += [f"    _{property_name}_wrapper_class: Type = {wrapper_class}"]
        if optional:
            result += [f"    _{property_name}_is_optional: bool = {optional}"]
        if choices:
            result += [f"    _{property_name}_choices: List[str] = {choices}"]
        if attributes:
            result += [f"    _{property_name}_attributes: List[str] = {attributes}"]
        if elements:
            result += [f"    _{property_name}_elements: List[str] = {elements}"]

        result += [""]
        result += [f"    @property"]
        result += [f"    def {property_name}(self) -> {pytype}:"]
        if doc:
            result += [f'        """']
            for line in doc.splitlines():
                result += [line]
            result += [f'        """']
        result += [f"        return self._get_element(\"{name}\"{property_name_kw})"]
        result += [""]
        result += [f"    @{property_name}.setter"]
        result += [f"    def {property_name}(self, value: {pytype}):"]
        result += [f"        self._set_element(\"{name}\", value{property_name_kw})"]
        result += [""]
        result += [f"    @{property_name}.deleter"]
        result += [f"    def {property_name}(self):"]
        result += [f"        self._delete_element(\"{name}\"{property_name_kw})"]

    # TODO: deleter
    # TODO: check if value is ok; if we can delete (mandatory)
    # TODO: attributes = lists 0+, 1+
    result += [""]
    return "\n".join(result)


def main():
    path = os.path.join(OBS_DIR, "docs/api/api/project.rng")
    parser = SchemaParser(path)
    parsed_schema = parser.parse()
    # print(parser.to_string())
    # print(parsed_schema)

    import glob
    import re
    path = os.path.join(OBS_DIR, "docs/api/api/project.rng")
    for path in [path]:
#    for path in glob.glob(os.path.join(OBS_DIR, "docs/api/api/*.rng")):
        # print(path)
        parser = SchemaParser(path)
        parsed_schema = parser.parse()

        defines = list(parsed_schema["defines"].keys())
        for define in defines:
            cls_name = re.sub("-element$", "", define)
            cls_name = "".join(i.capitalize() for i in cls_name.split("-"))
            o = parsed_schema_to_class(parsed_schema, define, cls_name)
            if not o.strip():
                print("SKIPPING", define)
                continue
            fn = "generated-classes/" + re.sub("-element$", "", define).replace("-", "_") + ".py"
            with open(fn, "w") as f:
                f.write(o)

#        parsed_schema_to_class

if __name__ == "__main__":
    main()
