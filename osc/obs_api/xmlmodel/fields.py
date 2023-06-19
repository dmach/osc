from .validators import ChoicesValidator
from .validators import TypeValidator
from .validators import OptionalValidator
from .xml import ET


class Field(property):
    def __init__(self, name, typ=None, optional=False, choices=None, help_text=None, validators=None):
        self.name = name
        self.typ = typ
        self.optional = optional
        self.choices = choices

        if help_text:
            help_text = "\n".join(help_text)
        else:
            help_text = None

        self.validators = [
            # FIXME: disable for now because many mandatory fields are not expected in tests yet
            # OptionalValidator(self),
            ChoicesValidator(self),
            TypeValidator(self),
        ]

        if validators:
            self.validators.extend(validators)

        super().__init__(fget=self.get, fset=self.set, fdel=self.delete, doc=help_text)

    def get(self, model):
        raise NotImplementedError()

    def set(self, model, values):
        raise NotImplementedError()

    def delete(self, model):
        raise NotImplementedError()

    def get_property_name(self, model):
        for name in dir(type(model)):
            prop = getattr(type(model), name)
            if type(prop) == type(self):
                return name
        raise RuntimeError("Couldn't determine property name")

    def validate(self, model, value, what=None):
        if what:
            what += f".{self.get_property_name(model)}"
        else:
            what = f"{self.get_property_name(model)}"

        for validator in self.validators:
            validator(value, what=what)


class DataField(Field):
    def get(self, model):
        typ = self.typ or str
        value = model._root.text
        if value is not None:
            value = typ(value)
        return value

    def set(self, model, value):
        for validator in self.validators:
            validator(value)

        if self.optional and value is None:
            self.delete(model)
        else:
            if value is not None:
                value = str(value)
            model._root.text = value

    def delete(self, model):
        model._root.text = None


class TagNameField(Field):
    def __init__(self, choices, help_text=None):
        super().__init__(name=None, choices=choices, help_text=help_text)

    def get(self, model):
        return model._root.tag

    def set(self, model, value):
        for validator in self.validators:
            validator(value)
        model._root.tag = value

    delete = None


class AttributeField(Field):
    def get(self, model):
        return model._root.attrib.get(self.name, None)

    def set(self, model, value):
        for validator in self.validators:
            validator(value)

        if self.optional and value is None:
            self.delete(model)
        else:
            model._root.attrib[self.name] = value

    def delete(self, model):
        model._root.attrib.pop(self.name)


class TextNodeField(Field):
    def get(self, model):
        node = model._root.find(self.name)
        if node is None:
            return None
        return node.text

    def set(self, model, value):
        for validator in self.validators:
            validator(value)

        self.delete(model)

        if value is None:
            # just delete the element
            return

        # create new node based on ``value``
        node = ET.SubElement(model._root, self.name)
        node.text = value

    def delete(self, model):
        nodes = model._root.findall(self.name)
        for node in nodes:
            model._root.remove(node)


class TextNodeListField(Field):
    def get(self, model):
        nodes = model._root.findall(self.name)
        if nodes is None:
            return ()
        return tuple([i.text for i in nodes])

    def set(self, model, values):
        # remove old nodes
        nodes = model._root.findall(self.name)
        for node in nodes:
            model._root.remove(node)

        # create new nodes based on ``values``
        for value in values:
            node = ET.SubElement(model._root, self.name)
            node.text = value

    def delete(self, model):
        pass

    def validate(self, model, values, what=None):
        if what:
            what += f".{self.get_property_name(model)}"
        else:
            what = f"{self.get_property_name(model)}"

        for validator in self.validators:
            for value in values:
                validator(value, what=what)


class ModelField(Field):
    def __init__(self, name, model_class, optional=False, help_text=None):
        super().__init__(name, optional=optional, help_text=None)
        self.model_class = model_class

    def get(self, model):
        result = []
        node = model._root.find(self.name)
        if node is not None:
            return self.model_class(node, tag_name=self.name)
        return None

    def set(self, model, value):
        assert type(value) == self.model_class, f"{type(value)} != {self.model_class}"

        self.delete(model)

        # The ``values`` contain objects encapsulating XML elements. Attach those to model's XML root.
        model._root.append(value._root)

    def delete(self, model):
        nodes = model._root.findall(self.name)
        for node in nodes:
            model._root.remove(node)

    def validate(self, model, value, what=None):
        if self.optional and value is None:
            return
        if what:
            what += f".{self.get_property_name(model)}"
        else:
            what = f"{self.get_property_name(model)}"

        value.validate(what=what)


class ModelListField(Field):
    def __init__(self, name, model_class, optional=False, outer_tag_name=None, help_text=None):
        super().__init__(name, optional=optional, help_text=None)
        self.model_class = model_class
        self.outer_tag_name = outer_tag_name

    def get(self, model):
        result = []

        if self.outer_tag_name:
            root = model._root.find(self.outer_tag_name)
            nodes = [] if root is None else root[:]
        else:
            nodes = model._root.findall(self.name)

        for node in nodes:
            entry = self.model_class(node)
            result.append(entry)
        return tuple(result)

    def set(self, model, values):
        for value in values:
            assert type(value) == self.model_class, f"{type(value)} != {self.model_class}"

        self.delete(model)

        if self.outer_tag_name:
            root = ET.SubElement(model._root, self.name)
        else:
            root = model._root

        # The ``values`` contain objects encapsulating XML elements. Attach those to model's XML root.
        for value in values:
            root.append(value._root)

    def delete(self, model):
        nodes = model._root.findall(self.name)
        for node in nodes:
            model._root.remove(node)

    def validate(self, model, values, what=None):
#        return
#        assert type(values) == tuple

        # TODO: validate 0+, 1+ etc.
        if what:
            what += f".{self.get_property_name(model)}"
        else:
            what = f"{self.get_property_name(model)}"

        for num, value in enumerate(values):
            value.validate(what=f"{what}[{num}]")


class EnableDisableField(Field):
    def __init__(self, name, optional=False, help_text=None):
        choices = ("enable", "disable")
        super().__init__(name, optional=optional, choices=choices, help_text=help_text)

    def get(self, model):
        node = model._root.find(self.name)
        if node is None or len(node) == 0:
            return None
        return node[0].tag

    def set(self, model, value):
        if value is True:
            value = "enable"
        elif value is False:
            value = "disable"

        for validator in self.validators:
            validator(value)

        self.delete(model)

        if value is None:
            # just delete the element
            return

        # create new nodes based on ``value``
        node = ET.SubElement(model._root, self.name)
        ET.SubElement(node, value)

    def delete(self, model):
        nodes = model._root.findall(self.name)
        for node in nodes:
            model._root.remove(node)