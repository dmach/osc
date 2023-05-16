from typing import List
from typing import Type

from . import _base
from .distribution import Distribution


class Distributions(_base.ApiEndPointBase):
    pass

    _elements: List[str] = ['distribution']
# {'list': '0+', 'ref': 'distribution-element'}

    _distributions_is_list: bool = True
    _distributions_wrapper_class: Type = Distribution

    @property
    def distributions(self) -> List[Distribution]:
        return self._get_element("distribution", property_name="distributions")

    @distributions.setter
    def distributions(self, value: List[Distribution]):
        self._set_element("distribution", value, property_name="distributions")

    @distributions.deleter
    def distributions(self):
        self._delete_element("distribution", property_name="distributions")
