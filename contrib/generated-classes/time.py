from typing import List
from typing import Type

from . import _base


class Time(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['file', 'build']

    @property
    def file(self) -> str:
        return self._get_attribute("file")

    @file.setter
    def file(self, value: str):
        self._set_attribute("file", value)

    @file.deleter
    def file(self):
        self._delete_attribute("file")

    @property
    def build(self) -> str:
        return self._get_attribute("build")

    @build.setter
    def build(self, value: str):
        self._set_attribute("build", value)

    @build.deleter
    def build(self):
        self._delete_attribute("build")
