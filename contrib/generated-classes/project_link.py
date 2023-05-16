from typing import List
from typing import Type

from . import _base


class ProjectLink(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['project', 'vrevmode']

    @property
    def project(self) -> str:
        return self._get_attribute("project")

    @project.setter
    def project(self, value: str):
        self._set_attribute("project", value)

    @project.deleter
    def project(self):
        self._delete_attribute("project")

    _vrevmode_is_optional: bool = True
    _vrevmode_choices: List[str] = ['unextend', 'extend']

    @property
    def vrevmode(self) -> str:
        return self._get_attribute("vrevmode")

    @vrevmode.setter
    def vrevmode(self, value: str):
        self._set_attribute("vrevmode", value)

    @vrevmode.deleter
    def vrevmode(self):
        self._delete_attribute("vrevmode")
