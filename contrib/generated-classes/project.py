from typing import List
from typing import Type

from . import _base
from .flag import Flag
from .group import Group
from .person import Person
from .project_link import ProjectLink
from .repository import Repository
from .simple_flag import SimpleFlag


class Project(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['name', 'kind']
    _elements: List[str] = ['title', 'description', 'url', 'link', 'mountproject', 'remoteurl', 'scmsync', 'devel', 'person', 'group', 'lock', 'build', 'publish', 'useforbuild', 'debuginfo', 'binarydownload', 'sourceaccess', 'access', 'maintenance', 'repository']

    @property
    def name(self) -> str:
        """
        The name of the project.
        """
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")

    _kind_is_optional: bool = True
    _kind_choices: List[str] = ['standard', 'maintenance', 'maintenance_incident', 'maintenance_release']

    @property
    def kind(self) -> str:
        """
        The kind (type) of the project.
        The default is ``standard``. Other kinds are ``maintenance``, ``maintenance_incident`` and ``maintenance_release``.

        Choices:
          - ``standard``
          - ``maintenance``
          - ``maintenance_incident``
          - ``maintenance_release``
        """
        return self._get_attribute("kind")

    @kind.setter
    def kind(self, value: str):
        self._set_attribute("kind", value)

    @kind.deleter
    def kind(self):
        self._delete_attribute("kind")
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
# {'list': '0+', 'ref': 'project-link-element'}

    _links_is_list: bool = True
    _links_wrapper_class: Type = ProjectLink

    @property
    def links(self) -> List[ProjectLink]:
        return self._get_element("link", property_name="links")

    @links.setter
    def links(self, value: List[ProjectLink]):
        self._set_element("link", value, property_name="links")

    @links.deleter
    def links(self):
        self._delete_element("link", property_name="links")
# {'optional': '1'}

    _mountproject_is_optional: bool = True

    @property
    def mountproject(self) -> str:
        return self._get_element("mountproject")

    @mountproject.setter
    def mountproject(self, value: str):
        self._set_element("mountproject", value)

    @mountproject.deleter
    def mountproject(self):
        self._delete_element("mountproject")
# {'optional': '1'}

    _remoteurl_is_optional: bool = True

    @property
    def remoteurl(self) -> str:
        return self._get_element("remoteurl")

    @remoteurl.setter
    def remoteurl(self, value: str):
        self._set_element("remoteurl", value)

    @remoteurl.deleter
    def remoteurl(self):
        self._delete_element("remoteurl")
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
# {'optional': '1', 'attributes': {'project': {}}}

    _devel_is_optional: bool = True
    _devel_attributes: List[str] = ['project']

    @property
    def devel(self) -> str:
        return self._get_element("devel")

    @devel.setter
    def devel(self, value: str):
        self._set_element("devel", value)

    @devel.deleter
    def devel(self):
        self._delete_element("devel")
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
# {'optional': '1', 'ref': 'simple-flag-element'}

    _access_wrapper_class: Type = SimpleFlag
    _access_is_optional: bool = True

    @property
    def access(self) -> SimpleFlag:
        return self._get_element("access")

    @access.setter
    def access(self, value: SimpleFlag):
        self._set_element("access", value)

    @access.deleter
    def access(self):
        self._delete_element("access")
# {'optional': '1', 'elements': {'maintains': {'list': '1+', 'attributes': {'project': {}}}}}

    _maintenance_is_optional: bool = True
    _maintenance_elements: List[str] = ['maintains']

    @property
    def maintenance(self) -> str:
        return self._get_element("maintenance")

    @maintenance.setter
    def maintenance(self, value: str):
        self._set_element("maintenance", value)

    @maintenance.deleter
    def maintenance(self):
        self._delete_element("maintenance")
# {'list': '0+', 'ref': 'repository-element'}

    _repositories_is_list: bool = True
    _repositories_wrapper_class: Type = Repository

    @property
    def repositories(self) -> List[Repository]:
        return self._get_element("repository", property_name="repositories")

    @repositories.setter
    def repositories(self, value: List[Repository]):
        self._set_element("repository", value, property_name="repositories")

    @repositories.deleter
    def repositories(self):
        self._delete_element("repository", property_name="repositories")
