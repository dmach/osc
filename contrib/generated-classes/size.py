from typing import List
from typing import Type

from . import _base


class Size(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['package', 'installed', 'archive']

    @property
    def package(self) -> str:
        return self._get_attribute("package")

    @package.setter
    def package(self, value: str):
        self._set_attribute("package", value)

    @package.deleter
    def package(self):
        self._delete_attribute("package")

    @property
    def installed(self) -> str:
        return self._get_attribute("installed")

    @installed.setter
    def installed(self, value: str):
        self._set_attribute("installed", value)

    @installed.deleter
    def installed(self):
        self._delete_attribute("installed")

    @property
    def archive(self) -> str:
        return self._get_attribute("archive")

    @archive.setter
    def archive(self, value: str):
        self._set_attribute("archive", value)

    @archive.deleter
    def archive(self):
        self._delete_attribute("archive")
