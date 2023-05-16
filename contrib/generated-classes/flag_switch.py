from typing import List
from typing import Type

from . import _base


class FlagSwitch(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['repository', 'arch']

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
