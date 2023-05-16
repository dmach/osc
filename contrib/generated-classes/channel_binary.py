from typing import List
from typing import Type

from . import _base


class ChannelBinary(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['name', 'binaryarch', 'project', 'repository', 'package', 'arch', 'supportstatus']

    @property
    def name(self) -> str:
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")

    _binaryarch_is_optional: bool = True

    @property
    def binaryarch(self) -> str:
        return self._get_attribute("binaryarch")

    @binaryarch.setter
    def binaryarch(self, value: str):
        self._set_attribute("binaryarch", value)

    @binaryarch.deleter
    def binaryarch(self):
        self._delete_attribute("binaryarch")

    _project_is_optional: bool = True

    @property
    def project(self) -> str:
        return self._get_attribute("project")

    @project.setter
    def project(self, value: str):
        self._set_attribute("project", value)

    @project.deleter
    def project(self):
        self._delete_attribute("project")

    _repository_is_optional: bool = True

    @property
    def repository(self) -> str:
        return self._get_attribute("repository")

    @repository.setter
    def repository(self, value: str):
        self._set_attribute("repository", value)

    @repository.deleter
    def repository(self):
        self._delete_attribute("repository")

    _package_is_optional: bool = True

    @property
    def package(self) -> str:
        return self._get_attribute("package")

    @package.setter
    def package(self, value: str):
        self._set_attribute("package", value)

    @package.deleter
    def package(self):
        self._delete_attribute("package")

    _arch_is_optional: bool = True

    @property
    def arch(self) -> str:
        return self._get_attribute("arch")

    @arch.setter
    def arch(self, value: str):
        self._set_attribute("arch", value)

    @arch.deleter
    def arch(self):
        self._delete_attribute("arch")

    _supportstatus_is_optional: bool = True

    @property
    def supportstatus(self) -> str:
        return self._get_attribute("supportstatus")

    @supportstatus.setter
    def supportstatus(self, value: str):
        self._set_attribute("supportstatus", value)

    @supportstatus.deleter
    def supportstatus(self):
        self._delete_attribute("supportstatus")
