from typing import List
from typing import Type

from . import _base
from .param import Param


class Service(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['name', 'mode']
    _elements: List[str] = ['param']

    @property
    def name(self) -> str:
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")

    _mode_is_optional: bool = True

    @property
    def mode(self) -> str:
        return self._get_attribute("mode")

    @mode.setter
    def mode(self, value: str):
        self._set_attribute("mode", value)

    @mode.deleter
    def mode(self):
        self._delete_attribute("mode")
# {'list': '0+', 'ref': 'param-element'}

    _params_is_list: bool = True
    _params_wrapper_class: Type = Param

    @property
    def params(self) -> List[Param]:
        return self._get_element("param", property_name="params")

    @params.setter
    def params(self, value: List[Param]):
        self._set_element("param", value, property_name="params")

    @params.deleter
    def params(self):
        self._delete_element("param", property_name="params")
