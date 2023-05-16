from typing import List
from typing import Type

from . import _base
from .constraint import Constraint


class Constraints(_base.ApiEndPointBase):
    pass

    _elements: List[str] = ['overwrite']
# {'list': '0+', 'elements': {'conditions': {'elements': {'arch': {'list': '0+', 'ref': 'build-arch'}, 'package': {'list': '0+'}}}}, 'ref': 'constraint-element'}

    _overwrites_is_list: bool = True
    _overwrites_wrapper_class: Type = Constraint
    _overwrites_elements: List[str] = ['conditions']

    @property
    def overwrites(self) -> List[Constraint]:
        return self._get_element("overwrite", property_name="overwrites")

    @overwrites.setter
    def overwrites(self, value: List[Constraint]):
        self._set_element("overwrite", value, property_name="overwrites")

    @overwrites.deleter
    def overwrites(self):
        self._delete_element("overwrite", property_name="overwrites")
