from typing import List
from typing import Type

from . import _base


class Group(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['groupid', 'role']

    @property
    def groupid(self) -> str:
        return self._get_attribute("groupid")

    @groupid.setter
    def groupid(self, value: str):
        self._set_attribute("groupid", value)

    @groupid.deleter
    def groupid(self):
        self._delete_attribute("groupid")

    @property
    def role(self) -> str:
        return self._get_attribute("role")

    @role.setter
    def role(self, value: str):
        self._set_attribute("role", value)

    @role.deleter
    def role(self):
        self._delete_attribute("role")
