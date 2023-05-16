from typing import List
from typing import Type

from . import _base


class KeyinfoPubkey(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['keyid', 'userid', 'algo', 'keysize', 'expires', 'fingerprint']

    @property
    def keyid(self) -> str:
        return self._get_attribute("keyid")

    @keyid.setter
    def keyid(self, value: str):
        self._set_attribute("keyid", value)

    @keyid.deleter
    def keyid(self):
        self._delete_attribute("keyid")

    @property
    def userid(self) -> str:
        return self._get_attribute("userid")

    @userid.setter
    def userid(self, value: str):
        self._set_attribute("userid", value)

    @userid.deleter
    def userid(self):
        self._delete_attribute("userid")

    @property
    def algo(self) -> str:
        return self._get_attribute("algo")

    @algo.setter
    def algo(self, value: str):
        self._set_attribute("algo", value)

    @algo.deleter
    def algo(self):
        self._delete_attribute("algo")

    @property
    def keysize(self) -> str:
        return self._get_attribute("keysize")

    @keysize.setter
    def keysize(self, value: str):
        self._set_attribute("keysize", value)

    @keysize.deleter
    def keysize(self):
        self._delete_attribute("keysize")

    @property
    def expires(self) -> str:
        return self._get_attribute("expires")

    @expires.setter
    def expires(self, value: str):
        self._set_attribute("expires", value)

    @expires.deleter
    def expires(self):
        self._delete_attribute("expires")

    @property
    def fingerprint(self) -> str:
        return self._get_attribute("fingerprint")

    @fingerprint.setter
    def fingerprint(self, value: str):
        self._set_attribute("fingerprint", value)

    @fingerprint.deleter
    def fingerprint(self):
        self._delete_attribute("fingerprint")
