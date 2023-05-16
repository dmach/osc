from typing import List
from typing import Type

from . import _base


class Person(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['userid', 'role']

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
    def role(self) -> str:
        return self._get_attribute("role")

    @role.setter
    def role(self, value: str):
        self._set_attribute("role", value)

    @role.deleter
    def role(self):
        self._delete_attribute("role")
