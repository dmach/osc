from typing import List
from typing import Type

from . import _base


class LocalizedString(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['lang']

    _lang_is_optional: bool = True

    @property
    def lang(self) -> str:
        return self._get_attribute("lang")

    @lang.setter
    def lang(self, value: str):
        self._set_attribute("lang", value)

    @lang.deleter
    def lang(self):
        self._delete_attribute("lang")
