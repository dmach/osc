from typing import List
from typing import Type

from . import _base


class SizeUnit(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['unit']

    _unit_choices: List[str] = ['K', 'M', 'G', 'T']

    @property
    def unit(self) -> str:
        return self._get_attribute("unit")

    @unit.setter
    def unit(self, value: str):
        self._set_attribute("unit", value)

    @unit.deleter
    def unit(self):
        self._delete_attribute("unit")
