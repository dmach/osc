from typing import List
from typing import Type

from . import _base


class KeyinfoSslcert(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['keyid', 'serial', 'issuer', 'subject', 'algo', 'keysize', 'begins', 'expires', 'fingerprint']

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
    def serial(self) -> str:
        return self._get_attribute("serial")

    @serial.setter
    def serial(self, value: str):
        self._set_attribute("serial", value)

    @serial.deleter
    def serial(self):
        self._delete_attribute("serial")

    @property
    def issuer(self) -> str:
        return self._get_attribute("issuer")

    @issuer.setter
    def issuer(self, value: str):
        self._set_attribute("issuer", value)

    @issuer.deleter
    def issuer(self):
        self._delete_attribute("issuer")

    @property
    def subject(self) -> str:
        return self._get_attribute("subject")

    @subject.setter
    def subject(self, value: str):
        self._set_attribute("subject", value)

    @subject.deleter
    def subject(self):
        self._delete_attribute("subject")

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
    def begins(self) -> str:
        return self._get_attribute("begins")

    @begins.setter
    def begins(self, value: str):
        self._set_attribute("begins", value)

    @begins.deleter
    def begins(self):
        self._delete_attribute("begins")

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
