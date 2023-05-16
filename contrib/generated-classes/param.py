from typing import List
from typing import Type

from . import _base


class Param(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['name']

    @property
    def name(self) -> str:
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")
