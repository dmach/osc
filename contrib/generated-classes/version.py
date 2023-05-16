from typing import List
from typing import Type

from . import _base


class Version(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['epoch', 'ver', 'rel']

    _epoch_is_optional: bool = True

    @property
    def epoch(self) -> str:
        return self._get_attribute("epoch")

    @epoch.setter
    def epoch(self, value: str):
        self._set_attribute("epoch", value)

    @epoch.deleter
    def epoch(self):
        self._delete_attribute("epoch")

    @property
    def ver(self) -> str:
        return self._get_attribute("ver")

    @ver.setter
    def ver(self, value: str):
        self._set_attribute("ver", value)

    @ver.deleter
    def ver(self):
        self._delete_attribute("ver")

    @property
    def rel(self) -> str:
        return self._get_attribute("rel")

    @rel.setter
    def rel(self, value: str):
        self._set_attribute("rel", value)

    @rel.deleter
    def rel(self):
        self._delete_attribute("rel")
