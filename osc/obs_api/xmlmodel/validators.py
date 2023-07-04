class ValidationError(Exception):
    def __init__(self, msg, what=None):
        if what:
            msg = f"{what}: {msg}"
        super().__init__(msg)
        self.xml = None

    def __str__(self):
        result = super().__str__()
        if self.xml:
            result += f"\n\nXML:\n{self.xml}"
        return result


class Validator:
    def __init__(self, field, model_name=None, property_name=None):
        self.field = field
        self.model_name = model_name
        self.property_name = property_name


class InvalidChoice(ValidationError):
    def __init__(self, value, all_choices, what=None):
        msg = f"Invalid value '{value}'. Valid choices are {all_choices}."
        super().__init__(msg, what)


class ChoicesValidator(Validator):
    def __call__(self, value, what=None):
        if not self.field.choices:
            return
        if value is None and self.field.optional:
            return
        if value not in self.field.choices:
            raise InvalidChoice(value, self.field.choices, what=what)


class InvalidType(ValidationError):
    def __init__(self, value, expected_type, what=None):
        msg = f"Invalid type '{type(value)}'. Expected type is {expected_type}."
        super().__init__(msg, what)


class TypeValidator(Validator):
    def __call__(self, value, what=None):
        if self.field.typ is None:
            return
        if value is None:
            return
        if not isinstance(value, self.field.typ):
            raise InvalidType(value, self.field.typ)


class ValueRequiredError(ValidationError):
    def __init__(self, what=None):
        msg = f"Field is mandatory but has no value."
        super().__init__(msg, what)


class OptionalValidator(Validator):
    def __call__(self, value, what=None):
        if self.field.optional:
            return
        if value is None:
            raise ValueRequiredError(what)
