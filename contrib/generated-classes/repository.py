from typing import List
from typing import Type

from . import _base
from .build_arch import BuildArch


class Repository(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['name', 'rebuild', 'block', 'linkedbuild']
    _elements: List[str] = ['download', 'releasetarget', 'hostsystem', 'path', 'arch']

    @property
    def name(self) -> str:
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")

    _rebuild_is_optional: bool = True

    @property
    def rebuild(self) -> str:
        return self._get_attribute("rebuild")

    @rebuild.setter
    def rebuild(self, value: str):
        self._set_attribute("rebuild", value)

    @rebuild.deleter
    def rebuild(self):
        self._delete_attribute("rebuild")

    _block_is_optional: bool = True

    @property
    def block(self) -> str:
        return self._get_attribute("block")

    @block.setter
    def block(self, value: str):
        self._set_attribute("block", value)

    @block.deleter
    def block(self):
        self._delete_attribute("block")

    _linkedbuild_is_optional: bool = True

    @property
    def linkedbuild(self) -> str:
        return self._get_attribute("linkedbuild")

    @linkedbuild.setter
    def linkedbuild(self, value: str):
        self._set_attribute("linkedbuild", value)

    @linkedbuild.deleter
    def linkedbuild(self):
        self._delete_attribute("linkedbuild")
# {'list': '0+', 'attributes': {'arch': {}, 'url': {}, 'repotype': {'choices': {'values': ['rpmmd', 'susetags', 'deb', 'arch', 'mdk', 'registry']}}}, 'elements': {'archfilter': {'optional': '1'}, 'master': {'optional': '1', 'attributes': {'url': {}, 'sslfingerprint': {'optional': '1'}}}, 'pubkey': {'optional': '1'}}}

    _downloads_is_list: bool = True
    _downloads_attributes: List[str] = ['arch', 'url', 'repotype']
    _downloads_elements: List[str] = ['archfilter', 'master', 'pubkey']

    @property
    def downloads(self) -> List[str]:
        return self._get_element("download", property_name="downloads")

    @downloads.setter
    def downloads(self, value: List[str]):
        self._set_element("download", value, property_name="downloads")

    @downloads.deleter
    def downloads(self):
        self._delete_element("download", property_name="downloads")
# {'list': '0+', 'attributes': {'project': {}, 'repository': {}, 'trigger': {'optional': '1', 'ref': 'release-triggers'}}}

    _releasetargets_is_list: bool = True
    _releasetargets_attributes: List[str] = ['project', 'repository', 'trigger']

    @property
    def releasetargets(self) -> List[str]:
        return self._get_element("releasetarget", property_name="releasetargets")

    @releasetargets.setter
    def releasetargets(self, value: List[str]):
        self._set_element("releasetarget", value, property_name="releasetargets")

    @releasetargets.deleter
    def releasetargets(self):
        self._delete_element("releasetarget", property_name="releasetargets")
# {'list': '0+', 'attributes': {'repository': {}, 'project': {}}}

    _hostsystems_is_list: bool = True
    _hostsystems_attributes: List[str] = ['repository', 'project']

    @property
    def hostsystems(self) -> List[str]:
        return self._get_element("hostsystem", property_name="hostsystems")

    @hostsystems.setter
    def hostsystems(self, value: List[str]):
        self._set_element("hostsystem", value, property_name="hostsystems")

    @hostsystems.deleter
    def hostsystems(self):
        self._delete_element("hostsystem", property_name="hostsystems")
# {'list': '0+', 'attributes': {'repository': {}, 'project': {}}}

    _paths_is_list: bool = True
    _paths_attributes: List[str] = ['repository', 'project']

    @property
    def paths(self) -> List[str]:
        return self._get_element("path", property_name="paths")

    @paths.setter
    def paths(self, value: List[str]):
        self._set_element("path", value, property_name="paths")

    @paths.deleter
    def paths(self):
        self._delete_element("path", property_name="paths")
# {'list': '0+', 'ref': 'build-arch'}

    _archs_is_list: bool = True
    _archs_wrapper_class: Type = BuildArch

    @property
    def archs(self) -> List[BuildArch]:
        return self._get_element("arch", property_name="archs")

    @archs.setter
    def archs(self, value: List[BuildArch]):
        self._set_element("arch", value, property_name="archs")

    @archs.deleter
    def archs(self):
        self._delete_element("arch", property_name="archs")
