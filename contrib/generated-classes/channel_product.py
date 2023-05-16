from typing import List
from typing import Type

from . import _base


class ChannelProduct(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['project', 'name']

    @property
    def project(self) -> str:
        return self._get_attribute("project")

    @project.setter
    def project(self, value: str):
        self._set_attribute("project", value)

    @project.deleter
    def project(self):
        self._delete_attribute("project")

    @property
    def name(self) -> str:
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")
