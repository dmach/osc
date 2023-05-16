from typing import List
from typing import Type

from . import _base


class Location(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['xml:base', 'href']

    _xml:base_is_optional: bool = True

    @property
    def xml:base(self) -> str:
        return self._get_attribute("xml:base")

    @xml:base.setter
    def xml:base(self, value: str):
        self._set_attribute("xml:base", value)

    @xml:base.deleter
    def xml:base(self):
        self._delete_attribute("xml:base")

    @property
    def href(self) -> str:
        return self._get_attribute("href")

    @href.setter
    def href(self, value: str):
        self._set_attribute("href", value)

    @href.deleter
    def href(self):
        self._delete_attribute("href")
