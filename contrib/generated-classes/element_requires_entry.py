from typing import List
from typing import Type

from . import _base


class ElementRequiresEntry(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['pre']

    _pre_is_optional: bool = True
    _pre_choices: List[str] = ['1', '0']

    @property
    def pre(self) -> str:
        return self._get_attribute("pre")

    @pre.setter
    def pre(self, value: str):
        self._set_attribute("pre", value)

    @pre.deleter
    def pre(self):
        self._delete_attribute("pre")
