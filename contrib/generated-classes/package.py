from typing import List
from typing import Type

from . import _base
from .flag import Flag
from .group import Group
from .person import Person
from .simple_flag import SimpleFlag


class Package(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['name', 'project']
    _elements: List[str] = ['title', 'description', 'devel', 'releasename', 'person', 'group', 'lock', 'build', 'publish', 'useforbuild', 'debuginfo', 'binarydownload', 'sourceaccess', 'url', 'scmsync', 'bcntsynctag']

    _name_is_optional: bool = True

    @property
    def name(self) -> str:
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")

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
# {}

    @property
    def title(self) -> str:
        return self._get_element("title")

    @title.setter
    def title(self, value: str):
        self._set_element("title", value)

    @title.deleter
    def title(self):
        self._delete_element("title")
# {}

    @property
    def description(self) -> str:
        return self._get_element("description")

    @description.setter
    def description(self, value: str):
        self._set_element("description", value)

    @description.deleter
    def description(self):
        self._delete_element("description")
# {'optional': '1', 'attributes': {'project': {'optional': '1'}, 'package': {'optional': '1'}}}

    _devel_is_optional: bool = True
    _devel_attributes: List[str] = ['project', 'package']

    @property
    def devel(self) -> str:
        return self._get_element("devel")

    @devel.setter
    def devel(self, value: str):
        self._set_element("devel", value)

    @devel.deleter
    def devel(self):
        self._delete_element("devel")
# {'optional': '1'}

    _releasename_is_optional: bool = True

    @property
    def releasename(self) -> str:
        return self._get_element("releasename")

    @releasename.setter
    def releasename(self, value: str):
        self._set_element("releasename", value)

    @releasename.deleter
    def releasename(self):
        self._delete_element("releasename")
# {'list': '0+', 'ref': 'person-element'}

    _persons_is_list: bool = True
    _persons_wrapper_class: Type = Person

    @property
    def persons(self) -> List[Person]:
        return self._get_element("person", property_name="persons")

    @persons.setter
    def persons(self, value: List[Person]):
        self._set_element("person", value, property_name="persons")

    @persons.deleter
    def persons(self):
        self._delete_element("person", property_name="persons")
# {'list': '0+', 'ref': 'group-element'}

    _groups_is_list: bool = True
    _groups_wrapper_class: Type = Group

    @property
    def groups(self) -> List[Group]:
        return self._get_element("group", property_name="groups")

    @groups.setter
    def groups(self, value: List[Group]):
        self._set_element("group", value, property_name="groups")

    @groups.deleter
    def groups(self):
        self._delete_element("group", property_name="groups")
# {'optional': '1', 'ref': 'simple-flag-element'}

    _lock_wrapper_class: Type = SimpleFlag
    _lock_is_optional: bool = True

    @property
    def lock(self) -> SimpleFlag:
        return self._get_element("lock")

    @lock.setter
    def lock(self, value: SimpleFlag):
        self._set_element("lock", value)

    @lock.deleter
    def lock(self):
        self._delete_element("lock")
# {'optional': '1', 'attributes': {'repository': {'optional': '1'}, 'arch': {'optional': '1', 'ref': 'build-arch'}}}

    _build_is_optional: bool = True
    _build_attributes: List[str] = ['repository', 'arch']

    @property
    def build(self) -> str:
        return self._get_element("build")

    @build.setter
    def build(self, value: str):
        self._set_element("build", value)

    @build.deleter
    def build(self):
        self._delete_element("build")
# {'optional': '1', 'attributes': {'repository': {'optional': '1'}, 'arch': {'optional': '1', 'ref': 'build-arch'}}}

    _publish_is_optional: bool = True
    _publish_attributes: List[str] = ['repository', 'arch']

    @property
    def publish(self) -> str:
        return self._get_element("publish")

    @publish.setter
    def publish(self, value: str):
        self._set_element("publish", value)

    @publish.deleter
    def publish(self):
        self._delete_element("publish")
# {'optional': '1', 'attributes': {'repository': {'optional': '1'}, 'arch': {'optional': '1', 'ref': 'build-arch'}}}

    _useforbuild_is_optional: bool = True
    _useforbuild_attributes: List[str] = ['repository', 'arch']

    @property
    def useforbuild(self) -> str:
        return self._get_element("useforbuild")

    @useforbuild.setter
    def useforbuild(self, value: str):
        self._set_element("useforbuild", value)

    @useforbuild.deleter
    def useforbuild(self):
        self._delete_element("useforbuild")
# {'optional': '1', 'attributes': {'repository': {'optional': '1'}, 'arch': {'optional': '1', 'ref': 'build-arch'}}}

    _debuginfo_is_optional: bool = True
    _debuginfo_attributes: List[str] = ['repository', 'arch']

    @property
    def debuginfo(self) -> str:
        return self._get_element("debuginfo")

    @debuginfo.setter
    def debuginfo(self, value: str):
        self._set_element("debuginfo", value)

    @debuginfo.deleter
    def debuginfo(self):
        self._delete_element("debuginfo")
# {'optional': '1', 'attributes': {'repository': {'optional': '1'}, 'arch': {'optional': '1', 'ref': 'build-arch'}}}

    _binarydownload_is_optional: bool = True
    _binarydownload_attributes: List[str] = ['repository', 'arch']

    @property
    def binarydownload(self) -> str:
        return self._get_element("binarydownload")

    @binarydownload.setter
    def binarydownload(self, value: str):
        self._set_element("binarydownload", value)

    @binarydownload.deleter
    def binarydownload(self):
        self._delete_element("binarydownload")
# {'optional': '1', 'ref': 'simple-flag-element'}

    _sourceaccess_wrapper_class: Type = SimpleFlag
    _sourceaccess_is_optional: bool = True

    @property
    def sourceaccess(self) -> SimpleFlag:
        return self._get_element("sourceaccess")

    @sourceaccess.setter
    def sourceaccess(self, value: SimpleFlag):
        self._set_element("sourceaccess", value)

    @sourceaccess.deleter
    def sourceaccess(self):
        self._delete_element("sourceaccess")
# {'optional': '1'}

    _url_is_optional: bool = True

    @property
    def url(self) -> str:
        return self._get_element("url")

    @url.setter
    def url(self, value: str):
        self._set_element("url", value)

    @url.deleter
    def url(self):
        self._delete_element("url")
# {'optional': '1'}

    _scmsync_is_optional: bool = True

    @property
    def scmsync(self) -> str:
        return self._get_element("scmsync")

    @scmsync.setter
    def scmsync(self, value: str):
        self._set_element("scmsync", value)

    @scmsync.deleter
    def scmsync(self):
        self._delete_element("scmsync")
# {'optional': '1'}

    _bcntsynctag_is_optional: bool = True

    @property
    def bcntsynctag(self) -> str:
        return self._get_element("bcntsynctag")

    @bcntsynctag.setter
    def bcntsynctag(self, value: str):
        self._set_element("bcntsynctag", value)

    @bcntsynctag.deleter
    def bcntsynctag(self):
        self._delete_element("bcntsynctag")
