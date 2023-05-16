from typing import List
from typing import Type

from . import _base
from .service import Service


class Services(_base.ApiEndPointBase):
    pass

    _elements: List[str] = ['service']
# {'list': '0+', 'ref': 'service-element'}

    _services_is_list: bool = True
    _services_wrapper_class: Type = Service

    @property
    def services(self) -> List[Service]:
        return self._get_element("service", property_name="services")

    @services.setter
    def services(self, value: List[Service]):
        self._set_element("service", value, property_name="services")

    @services.deleter
    def services(self):
        self._delete_element("service", property_name="services")
