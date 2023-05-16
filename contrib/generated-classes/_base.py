from xml.etree import ElementTree as ET


class ApiEndPointBase:
    def __init__(self, xml_node, apiurl=None):
        self.__dict__["root"] = xml_node
        self.__dict__["apiurl"] = apiurl

    def __setattr__(self, name, value):
        if hasattr(self.__class__, name):
            # allow setting properties - test if they exist in the class
            return super().__setattr__(name, value)
        raise AttributeError(f"Setting attribute '{self.__class__.__name__}.{name}' is not allowed")

    @staticmethod
    def _sort_elements(node, order):
        """
        
        """
        if not order:
            return

        elems = node[:]

        def indx(item):
            try:
                return order.index(item.tag)
            except ValueError as e:
                return 9999

        elems.sort(key=indx)
        node[:] = elems

    def _reindent(self, node):
        node.tail = ""
        if node.text:
            node.text = node.text.strip()
        for child in node[:]:
            self._reindent(child)

    def _validate(self):
        pass

    def to_bytes(self):
        """
        Return the object as XML in form of utf-8 encoded bytes.
        """
        self._validate()
        self._sort_elements(self.root, self._elements)
        self._reindent(self.root)
        ET.indent(self.root, space="  ", level=0)
        return ET.tostring(self.root, encoding="utf-8", short_empty_elements=True)

    def to_string(self):
        return self.to_bytes().decode("utf-8")

    @classmethod
    def from_string(cls, text):
        root = ET.fromstring(text)
        return cls(root)

#    @staticmethod
#    def _get_property_name(name, plural=False):
#        name = name.replace("-", "_")
#        if plural:
#            if name.endswith("y"):
#                name = name[:-1]
#                name = f"{name}ies"
#            else:
#                name = f"{name}s"
#        return name

    def _get_attribute(self, name, property_name=None):
        property_name = property_name or name
        return self.root.attrib.get(name, None)

    def _set_attribute(self, name, value, property_name=None):
        property_name = property_name or name
        if value is None:
            self._delete_attribute(name, property_name)
            return

        choices = getattr(self, f"_{property_name}_choices", [])
        if choices:
            if value not in choices:
                raise ValueError(f"choice, {value}, {choices}")
        self.root.attrib[name] = value

    def _delete_attribute(self, name, property_name=None):
        property_name = property_name or name
        optional = getattr(self, f"_{property_name}_is_optional", False)
        if not optional:
            raise ValueError("attr is mandatory " + name)
        del self.root.attrib[name]

    def _get_element(self, name, property_name=None):
        property_name = property_name or name
        is_list = getattr(self, f"_{property_name}_is_list", False)
        wrapper_class = getattr(self, f"_{property_name}_wrapper_class", None)
#        choices = getattr(self, f"_{property_name}_choices", [])
        attributes = getattr(self, f"_{property_name}_attributes", [])
#        elements = getattr(self, f"_{property_name}_elements", [])
#        is_choices = bool(getattr(wrapper_class, "_choices", None))

        nodes = self.root.findall(name)

        result = []
        for node in nodes:
            if wrapper_class:
                obj = wrapper_class(node)
                if hasattr(obj, "get"):
                    # choices that return simple values
                    result.append(obj.get())
                else:
                    # wrapper object that provides access to other elements
                    result.append(obj)
            elif attributes:
                # dict with attributes
                # TODO: shouldn't it be wrapped into a class?
                entry = {}
                for attribute in attributes:
                    if attribute in node.attrib:
                        entry[attribute] = node.attrib[attribute]
                result.append(entry)
                print("append", entry)
            else:
                result.append(node.text)

        if is_list:
            return tuple(result)

        if not result:
            return None
        return result[0]

    def _set_element(self, name, value, property_name=None):
        property_name = property_name or name
        if value in (None, []):
            self._delete_element(name, property_name)
            return

        is_list = getattr(self, f"_{property_name}_is_list", False)
        wrapper_class = getattr(self, f"_{property_name}_wrapper_class", None)
        choices = getattr(self, f"_{property_name}_choices", [])
        attributes = getattr(self, f"_{property_name}_attributes", [])
        elements = getattr(self, f"_{property_name}_elements", [])

        if is_list:
            values = value
        else:
            values = [value]

        # remove old nodes
        nodes = self.root.findall(name)
        for node in nodes:
            self.root.remove(node)

        # create new node(s) based on ``value``
        for val in values:
            node = ET.SubElement(self.root, name)

            if wrapper_class:
                obj = wrapper_class(node)
                if hasattr(obj, "set"):
                    obj.set(value)
                else:
                    raise ValueError("cannot be set ???")
                    print("!!!", wrapper_class, node)
                    11/0
            elif len(elements) == 1 and attributes:
                1234/0
            elif attributes:
#                print("VALS", values)
#                for entry in values:
#                    node = ET.SubElement(self.root, name)
                for key in val:
                    if key not in attributes:
                        raise ValueError(key)
                node.attrib.update(val)
#                    print("NN", node, node.attrib, self.root.tag)
#                    result.append(node)
#
#                attribute in attributes:
#                    if attribute in node.attrib:
#                        entry[attribute] = node.attrib[attribute]
#                result.append(entry)
#                print("append", entry)

            else:
                node.text = value

#        self._sort_elements(self.root, self._elements)
        return
            
#        for val in values:
#            if wrapper_class and not isinstance(val, wrapper_class):
#                raise TypeError(val)

        if not is_list:
            node = self.root.find(name)
            if node is None:
                node = ET.SubElement(self.root, name)

            if wrapper_class:
                obj = wrapper_class(node)
                obj.set(value)
            else:
#            if choices:
#                if value not in choices:
#                    raise ValueError(f"choice, {value}, {choices}")
                node.text = value
            return

        if choices:
            if set(value) - set(choices):
                raise ValueError(f"choice, {value}, {choices}")
        nodes = self.root.findall(name)
        if nodes:
            indx = self.root[:].index(nodes[0])
            for i in nodes:
                self.root.remove(i)
        else:
            indx = len(self.root) - 1
        for i in value:
            new_node = ET.SubElement(self.root, name)
            if isinstance(i, str):
                new_node.text = i
            else:
                for key, value in i.items():
                    new_node.attrib[key] = value
            self._sort_elements(new_node, elements)
            print(self, self.root, self._elements)
            self._sort_elements(self.root, self._elements)
            self.root[indx:indx] = new_node

    def _delete_element(self, name, property_name=None):
        property_name = property_name or name
        optional = getattr(self, f"_{property_name}_is_optional", False)
        if not optional:
            raise ValueError("element is mandatory " + name)
        for node in self.root.findall(name):
            self.root.remove(node)


class InvalidChoice(ValueError):
    def __init__(self, value, all_choices):
        msg = f"Invalid value '{value}'. Valid choices are {all_choices}"
        super().__init__(msg)


class Choices(ApiEndPointBase):
    """
    Choices represented as strings in the resulting XML: <node>choice_value</node>
    """
    def set(self, value):
        if value not in self._choices:
            raise InvalidChoice(value, self._choices)
        self.root.text = value

    def get(self):
        return self.root.text


class ElementChoices(ApiEndPointBase):
    """
    Choices represented as elements in the resulting XML: <node><choice_value /></node>
    """
    def set(self, value):
        if value not in self._elements:
            raise InvalidChoice(value, self._elements)
        self.root.clear()
        from xml.etree import ElementTree as ET
        ET.SubElement(self.root, value)
#        print(self.root.getchildren())

    def get(self):
#        print("ROOT", dir(self.root))
        #children = self.root.getchildren()
        assert len(self.root) <= 1
        l = len(self.root)
        if l == 0:
            return None
        elif l == 1:
            return self.root[0].tag
        else:
            raise RuntimeError("ASD")


class Flag(ApiEndPointBase):
    def get(self):
        result = []
        for node in self.root:
            entry = {"flag": node.tag}
            for key in ["repository", "arch"]:
                if key in node.attrib:
                    entry[key] = node.attrib[key]
            result.append(entry)
        return tuple(result)

    def set(self, value):
        # TODO: check keys

        self.root.clear()

        for entry in value:
            flag = entry["flag"]
            repository = entry.get("repository", None)
            arch = entry.get("arch", None)
            from xml.etree import ElementTree as ET
            node = ET.SubElement(self.root, flag)
            if repository:
                node.attrib["repository"] = repository
            if arch:
                node.attrib["arch"] = arch


'''
class Flag(ApiEndPointBase):
    #state = ChoicesBase
#    state = None
#    repository = None
#    arch = None
    @property
    def state(self):
        return self.root.tag

    @property
    def arch(self):
        return self.root.attrib.get("arch", None)

    @property
    def repository(self):
        return self.root.attrib.get("repository", None)
'''
