from typing import List
from typing import Type

from . import _base
from .element_pattern import ElementPattern


class ElementPatterns(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['count']
    _elements: List[str] = ['pattern']

    _count_is_optional: bool = True

    @property
    def count(self) -> str:
        return self._get_attribute("count")

    @count.setter
    def count(self, value: str):
        self._set_attribute("count", value)

    @count.deleter
    def count(self):
        self._delete_attribute("count")
# {'list': '1+', 'ref': 'element-pattern'}

    _patterns_is_list: bool = True
    _patterns_wrapper_class: Type = ElementPattern

    @property
    def patterns(self) -> List[ElementPattern]:
        return self._get_element("pattern", property_name="patterns")

    @patterns.setter
    def patterns(self, value: List[ElementPattern]):
        self._set_element("pattern", value, property_name="patterns")

    @patterns.deleter
    def patterns(self):
        self._delete_element("pattern", property_name="patterns")
