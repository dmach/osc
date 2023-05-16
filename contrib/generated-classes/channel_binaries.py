from typing import List
from typing import Type

from . import _base
from .channel_binary import ChannelBinary


class ChannelBinaries(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['project', 'repository', 'arch']
    _elements: List[str] = ['binary']

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
# {'list': '1+', 'ref': 'channel-binary-element'}

    _binaries_is_list: bool = True
    _binaries_wrapper_class: Type = ChannelBinary

    @property
    def binaries(self) -> List[ChannelBinary]:
        return self._get_element("binary", property_name="binaries")

    @binaries.setter
    def binaries(self, value: List[ChannelBinary]):
        self._set_element("binary", value, property_name="binaries")

    @binaries.deleter
    def binaries(self):
        self._delete_element("binary", property_name="binaries")
