from typing import List
from typing import Type

from . import _base
from .parameter import Parameter


class ServiceDef(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['name']
    _elements: List[str] = ['summary', 'description', 'parameter']

    @property
    def name(self) -> str:
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")
# {'doc': 'Summary of service purpose.'}

    @property
    def summary(self) -> str:
        """
        Summary of service purpose.
        """
        return self._get_element("summary")

    @summary.setter
    def summary(self, value: str):
        self._set_element("summary", value)

    @summary.deleter
    def summary(self):
        self._delete_element("summary")
# {'doc': 'Longer description of service purpose.'}

    @property
    def description(self) -> str:
        """
        Longer description of service purpose.
        """
        return self._get_element("description")

    @description.setter
    def description(self, value: str):
        self._set_element("description", value)

    @description.deleter
    def description(self):
        self._delete_element("description")
# {'list': '0+', 'ref': 'parameter-element'}

    _parameters_is_list: bool = True
    _parameters_wrapper_class: Type = Parameter

    @property
    def parameters(self) -> List[Parameter]:
        return self._get_element("parameter", property_name="parameters")

    @parameters.setter
    def parameters(self, value: List[Parameter]):
        self._set_element("parameter", value, property_name="parameters")

    @parameters.deleter
    def parameters(self):
        self._delete_element("parameter", property_name="parameters")
