from typing import List
from typing import Type

from . import _base


class Checksum(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['type', 'pkgid']

    _type_choices: List[str] = ['md5', 'sha']

    @property
    def type(self) -> str:
        return self._get_attribute("type")

    @type.setter
    def type(self, value: str):
        self._set_attribute("type", value)

    @type.deleter
    def type(self):
        self._delete_attribute("type")

    _pkgid_choices: List[str] = ['YES', 'NO']

    @property
    def pkgid(self) -> str:
        return self._get_attribute("pkgid")

    @pkgid.setter
    def pkgid(self, value: str):
        self._set_attribute("pkgid", value)

    @pkgid.deleter
    def pkgid(self):
        self._delete_attribute("pkgid")
