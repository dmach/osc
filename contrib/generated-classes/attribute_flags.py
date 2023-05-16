from typing import List
from typing import Type

from . import _base


class AttributeFlags(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['flags']

    _flags_choices: List[str] = ['EQ', 'LE', 'GE', 'LT', 'GT']

    @property
    def flags(self) -> str:
        return self._get_attribute("flags")

    @flags.setter
    def flags(self, value: str):
        self._set_attribute("flags", value)

    @flags.deleter
    def flags(self):
        self._delete_attribute("flags")
