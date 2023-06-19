from . import xml
from .fields import Field
from .validators import ValidationError
from .xml import ET


class Model:
    TAG_NAME = None

    @classmethod
    def new(cls, **kwargs):
        root = ET.Element(cls.TAG_NAME)
        obj = cls(root)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        return obj

    @classmethod
    def from_string(cls, text):
        root = ET.fromstring(text)
        return cls(root)

    @classmethod
    def from_file(cls, file_path_or_object):
        root = ET.parse(file_path_or_object)
        return cls(root)

    def __init__(self, root, tag_name=None):
        self.__dict__["_tag_name"] = tag_name or self.TAG_NAME
        if not self._tag_name:
            raise RuntimeError("tag_name is not set")

        tag_is_valid = False
        if isinstance(self._tag_name, tuple) and root.tag in self._tag_name:
            tag_is_valid = True
        elif root.tag == self._tag_name:
            tag_is_valid = True

        if not tag_is_valid:
            raise RuntimeError(f"Invalid XML element '{root.tag}'. Expecting '{self._tag_name}'")

        self.__dict__["_root"] = root

    def __setattr__(self, name, value):
        if hasattr(self.__class__, name):
            # allow setting properties - test if they exist in the class
            return super().__setattr__(name, value)
        raise AttributeError(f"Setting attribute '{self.__class__.__name__}.{name}' is not allowed")

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
                self.root.write(f, encoding="utf-8")
        else:
            self.root.write(file_path_or_object, encoding="utf-8")

    def _iter_fields(self):
        for name in dir(type(self)):
            field = getattr(type(self), name)
            if not isinstance(field, Field):
                continue
            yield name, field

    def validate(self, what=None):
        if not what:
            what = self.__class__.__name__

        for name, field in self._iter_fields():
            value = getattr(self, name)
            try:
                field.validate(self, value, what=what)
            except ValidationError as ex:
                # inject XML to the exception so we can report it to the user for debugging purposes
                ex.xml = self.to_string(validate=False)
                raise

    def _pre_save(self):

# TODO: generate empty values for mandatory field
#        for name, field in self._iter_fields():
#            if field.optional:
#                continue
#            value = getattr(self, name)
#            if not value:
#                setattr(self, name, "")

        self.validate()
# TODO: recursively sort elements by field order
#        self._sort_elements(self.root, self._elements)
        self._reindent(self._root)
        xml.indent(self._root)
        pass

    def _reindent(self, node):
        node.tail = ""
        if node.text:
            node.text = node.text.strip()
        for child in node[:]:
            self._reindent(child)
