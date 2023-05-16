from typing import List
from typing import Type

from . import _base


class Dirsize(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['path', 'size-kbyte', 'filecount']

    @property
    def path(self) -> str:
        return self._get_attribute("path")

    @path.setter
    def path(self, value: str):
        self._set_attribute("path", value)

    @path.deleter
    def path(self):
        self._delete_attribute("path")

    @property
    def size_kbyte(self) -> str:
        return self._get_attribute("size-kbyte", property_name="size_kbyte")

    @size_kbyte.setter
    def size_kbyte(self, value: str):
        self._set_attribute("size-kbyte", value, property_name="size_kbyte")

    @size_kbyte.deleter
    def size_kbyte(self):
        self._delete_attribute("size-kbyte", property_name="size_kbyte")

    @property
    def filecount(self) -> str:
        return self._get_attribute("filecount")

    @filecount.setter
    def filecount(self, value: str):
        self._set_attribute("filecount", value)

    @filecount.deleter
    def filecount(self):
        self._delete_attribute("filecount")
