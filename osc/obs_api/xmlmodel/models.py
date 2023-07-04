import functools

from . import xml
from .fields import Field
from .validators import ValidationError
from .xml import ET


@functools.total_ordering
class Model:
    TAG_NAME: str = None

    def __init__(self, _root=None, **kwargs):
        # create empty attributes and assign to them later to mute pylint error E1101 (no-member)
        self.__dict__["_apiurl"] = None
        self.__dict__["_fields"] = {}
        self.__dict__["_root"] = None

        if not self.TAG_NAME:
            raise RuntimeError("TAG_NAME is not set")

        self._root = _root if _root is not None else ET.Element(self.TAG_NAME)

        tag_is_valid = False
        if isinstance(self.TAG_NAME, tuple) and self._root.tag in self.TAG_NAME:
            tag_is_valid = True
        elif self._root.tag == self.TAG_NAME:
            tag_is_valid = True

        if not tag_is_valid:
            raise RuntimeError(f"Invalid XML element '{self._root.tag}'. Expecting '{self.TAG_NAME}'")

        for key, value in kwargs.items():
            if value is None:
                continue
            setattr(self, key, value)

    def __setattr__(self, name, value):
        if hasattr(self.__class__, name) or hasattr(self, name):
            # allow setting properties - test if they exist in the class
            # also allow setting existing attributes that were previously initialized via __dict__
            return super().__setattr__(name, value)
        raise AttributeError(f"Setting attribute '{self.__class__.__name__}.{name}' is not allowed")

    def __eq__(self, other):
        self_data = [value for _, value in self.iter_field_names_values()]
        other_data = [value for _, value in other.iter_field_names_values()]
        return self_data == other_data

    def __lt__(self, other):
        self_data = [value for _, value in self.iter_field_names_values()]
        other_data = [value for _, value in other.iter_field_names_values()]
        return self_data < other_data

    @classmethod
    def from_string(cls, text):
        root = ET.fromstring(text)
        return cls(_root=root)

    @classmethod
    def from_file(cls, file_path_or_object):
        doc = ET.parse(file_path_or_object)
        root = doc.getroot()
        return cls(_root=root)

    def to_bytes(self, validate=True):
        """
        Return the object as XML in form of utf-8 encoded bytes.
        """
        if validate:
            self._pre_save()
        ET.indent(self._root, space="  ", level=0)
        return ET.tostring(self._root, encoding="utf-8", short_empty_elements=True)

    def to_string(self, validate=True):
        return self.to_bytes(validate=validate).decode("utf-8")

    def to_file(self, file_path_or_object):
        self._pre_save()
        if isinstance(file_path_or_object, str):
            with open(file_path_or_object, "wb") as f:
                self._root.write(f, encoding="utf-8")
        else:
            self._root.write(file_path_or_object, encoding="utf-8")

    def iter_field_names_objects(self):
        """
        Iterate through (field name, field object) pairs.
        """
        # TODO: iterate in reversed order?
        # TODO: test handling deleted properties in derived classes
        # NOTE: dir() doesn't preserve attribute order; we need to iterate through __mro__ classes to workaround that
        if not self._fields:
            for i in reversed(type(self).__mro__):
                for name in i.__dict__:
                    if name in self._fields:
                        continue
                    field = getattr(type(self), name)
                    if not isinstance(field, Field):
                        continue
                    self._fields[name] = field
        yield from self._fields.items()

    def iter_field_names_values(self):
        """
        Iterate through (field name, field value) pairs.
        """
        for name, _ in self.iter_field_names_objects():
            value = getattr(self, name)
            yield name, value

    def validate(self, what=None):
        if not what:
            what = self.__class__.__name__

        for name, field in self.iter_field_names_objects():
            value = getattr(self, name)
            try:
                field.validate(self, value, what=what)
            except ValidationError as ex:
                # inject XML to the exception so we can report it to the user for debugging purposes
                ex.xml = name
                ex.xml = self.to_string(validate=False)
                raise

    def _pre_save(self):
        self.validate()
#        self._sort_nodes()
        self._reindent(self._root)
        xml.indent(self._root)

    def _sort_nodes(self):
        node_order = [field.name for _, field in self.iter_field_names_objects()]
        nodes = self._root[:]
        nodes.sort(key=lambda x: node_order.index(x.tag))
        self._root[:] = nodes

        for name, field in self.iter_field_names_objects():
            if not getattr(field, "model_class", None):
                continue
            value = getattr(self, name)
            if value is None:
                continue
            if isinstance(value, tuple):
                for i in value:
                    i._sort_nodes()
            else:
                value._sort_nodes()

    def _reindent(self, node):
        node.tail = ""
        if node.text:
            node.text = node.text.strip()
        for child in node[:]:
            self._reindent(child)
