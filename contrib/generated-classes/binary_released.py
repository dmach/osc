from typing import List
from typing import Type

from . import _base
from .supportstatus_choices import SupportstatusChoices


class Binary_released(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['project', 'repository', 'name', 'epoch', 'version', 'release', 'arch', 'medium']
    _elements: List[str] = ['operation', 'publish', 'medium', 'build', 'modify', 'obsolete', 'supportstatus', 'updateinfo', 'maintainer', 'disturl', 'binaryid', 'updatefor']

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
    def repository(self) -> str:
        return self._get_attribute("repository")

    @repository.setter
    def repository(self, value: str):
        self._set_attribute("repository", value)

    @repository.deleter
    def repository(self):
        self._delete_attribute("repository")

    @property
    def name(self) -> str:
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")

    _epoch_is_optional: bool = True

    @property
    def epoch(self) -> str:
        return self._get_attribute("epoch")

    @epoch.setter
    def epoch(self, value: str):
        self._set_attribute("epoch", value)

    @epoch.deleter
    def epoch(self):
        self._delete_attribute("epoch")

    @property
    def version(self) -> str:
        return self._get_attribute("version")

    @version.setter
    def version(self, value: str):
        self._set_attribute("version", value)

    @version.deleter
    def version(self):
        self._delete_attribute("version")

    @property
    def release(self) -> str:
        return self._get_attribute("release")

    @release.setter
    def release(self, value: str):
        self._set_attribute("release", value)

    @release.deleter
    def release(self):
        self._delete_attribute("release")

    @property
    def arch(self) -> str:
        return self._get_attribute("arch")

    @arch.setter
    def arch(self, value: str):
        self._set_attribute("arch", value)

    @arch.deleter
    def arch(self):
        self._delete_attribute("arch")

    _medium_is_optional: bool = True

    @property
    def medium(self) -> str:
        return self._get_attribute("medium")

    @medium.setter
    def medium(self, value: str):
        self._set_attribute("medium", value)

    @medium.deleter
    def medium(self):
        self._delete_attribute("medium")
# {'choices': {'values': ['added', 'modified']}}

    _operation_choices: List[str] = ['added', 'modified']

    @property
    def operation(self) -> str:
        return self._get_element("operation")

    @operation.setter
    def operation(self, value: str):
        self._set_element("operation", value)

    @operation.deleter
    def operation(self):
        self._delete_element("operation")
# {'optional': '1', 'attributes': {'project': {'optional': '1'}, 'package': {}, 'time': {}}}

    _publish_is_optional: bool = True
    _publish_attributes: List[str] = ['project', 'package', 'time']

    @property
    def publish(self) -> str:
        return self._get_element("publish")

    @publish.setter
    def publish(self, value: str):
        self._set_element("publish", value)

    @publish.deleter
    def publish(self):
        self._delete_element("publish")
# {'optional': '1', 'attributes': {'project': {}, 'package': {}}}

    _medium_is_optional: bool = True
    _medium_attributes: List[str] = ['project', 'package']

    @property
    def medium(self) -> str:
        return self._get_element("medium")

    @medium.setter
    def medium(self, value: str):
        self._set_element("medium", value)

    @medium.deleter
    def medium(self):
        self._delete_element("medium")
# {'optional': '1', 'attributes': {'time': {}}}

    _build_is_optional: bool = True
    _build_attributes: List[str] = ['time']

    @property
    def build(self) -> str:
        return self._get_element("build")

    @build.setter
    def build(self, value: str):
        self._set_element("build", value)

    @build.deleter
    def build(self):
        self._delete_element("build")
# {'optional': '1', 'attributes': {'time': {}}}

    _modify_is_optional: bool = True
    _modify_attributes: List[str] = ['time']

    @property
    def modify(self) -> str:
        return self._get_element("modify")

    @modify.setter
    def modify(self, value: str):
        self._set_element("modify", value)

    @modify.deleter
    def modify(self):
        self._delete_element("modify")
# {'optional': '1', 'attributes': {'time': {}}}

    _obsolete_is_optional: bool = True
    _obsolete_attributes: List[str] = ['time']

    @property
    def obsolete(self) -> str:
        return self._get_element("obsolete")

    @obsolete.setter
    def obsolete(self, value: str):
        self._set_element("obsolete", value)

    @obsolete.deleter
    def obsolete(self):
        self._delete_element("obsolete")
# {'optional': '1', 'ref': 'supportstatus-choices'}

    _supportstatus_wrapper_class: Type = SupportstatusChoices
    _supportstatus_is_optional: bool = True

    @property
    def supportstatus(self) -> SupportstatusChoices:
        return self._get_element("supportstatus")

    @supportstatus.setter
    def supportstatus(self, value: SupportstatusChoices):
        self._set_element("supportstatus", value)

    @supportstatus.deleter
    def supportstatus(self):
        self._delete_element("supportstatus")
# {'optional': '1', 'attributes': {'id': {}, 'version': {}}}

    _updateinfo_is_optional: bool = True
    _updateinfo_attributes: List[str] = ['id', 'version']

    @property
    def updateinfo(self) -> str:
        return self._get_element("updateinfo")

    @updateinfo.setter
    def updateinfo(self, value: str):
        self._set_element("updateinfo", value)

    @updateinfo.deleter
    def updateinfo(self):
        self._delete_element("updateinfo")
# {'optional': '1'}

    _maintainer_is_optional: bool = True

    @property
    def maintainer(self) -> str:
        return self._get_element("maintainer")

    @maintainer.setter
    def maintainer(self, value: str):
        self._set_element("maintainer", value)

    @maintainer.deleter
    def maintainer(self):
        self._delete_element("maintainer")
# {'optional': '1'}

    _disturl_is_optional: bool = True

    @property
    def disturl(self) -> str:
        return self._get_element("disturl")

    @disturl.setter
    def disturl(self, value: str):
        self._set_element("disturl", value)

    @disturl.deleter
    def disturl(self):
        self._delete_element("disturl")
# {'optional': '1'}

    _binaryid_is_optional: bool = True

    @property
    def binaryid(self) -> str:
        return self._get_element("binaryid")

    @binaryid.setter
    def binaryid(self, value: str):
        self._set_element("binaryid", value)

    @binaryid.deleter
    def binaryid(self):
        self._delete_element("binaryid")
# {'optional': '1', 'attributes': {'project': {}, 'product': {}}}

    _updatefor_is_optional: bool = True
    _updatefor_attributes: List[str] = ['project', 'product']

    @property
    def updatefor(self) -> str:
        return self._get_element("updatefor")

    @updatefor.setter
    def updatefor(self, value: str):
        self._set_element("updatefor", value)

    @updatefor.deleter
    def updatefor(self):
        self._delete_element("updatefor")
