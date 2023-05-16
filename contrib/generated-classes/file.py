from typing import List
from typing import Type

from . import _base


class File(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['type']

    _type_is_optional: bool = True
    _type_choices: List[str] = ['dir', 'ghost']

    @property
    def type(self) -> str:
        return self._get_attribute("type")

    @type.setter
    def type(self, value: str):
        self._set_attribute("type", value)

    @type.deleter
    def type(self):
        self._delete_attribute("type")
