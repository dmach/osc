from typing import List
from typing import Type

from . import _base
from .architecture import Architecture
from .icon import Icon


class Distribution(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['id', 'vendor', 'version']
    _elements: List[str] = ['name', 'project', 'repository', 'reponame', 'architecture', 'icon', 'link']

    _id_is_optional: bool = True

    @property
    def id(self) -> str:
        return self._get_attribute("id")

    @id.setter
    def id(self, value: str):
        self._set_attribute("id", value)

    @id.deleter
    def id(self):
        self._delete_attribute("id")

    @property
    def vendor(self) -> str:
        return self._get_attribute("vendor")

    @vendor.setter
    def vendor(self, value: str):
        self._set_attribute("vendor", value)

    @vendor.deleter
    def vendor(self):
        self._delete_attribute("vendor")

    @property
    def version(self) -> str:
        return self._get_attribute("version")

    @version.setter
    def version(self, value: str):
        self._set_attribute("version", value)

    @version.deleter
    def version(self):
        self._delete_attribute("version")
# {}

    @property
    def name(self) -> str:
        return self._get_element("name")

    @name.setter
    def name(self, value: str):
        self._set_element("name", value)

    @name.deleter
    def name(self):
        self._delete_element("name")
# {}

    @property
    def project(self) -> str:
        return self._get_element("project")

    @project.setter
    def project(self, value: str):
        self._set_element("project", value)

    @project.deleter
    def project(self):
        self._delete_element("project")
# {}

    @property
    def repository(self) -> str:
        return self._get_element("repository")

    @repository.setter
    def repository(self, value: str):
        self._set_element("repository", value)

    @repository.deleter
    def repository(self):
        self._delete_element("repository")
# {}

    @property
    def reponame(self) -> str:
        return self._get_element("reponame")

    @reponame.setter
    def reponame(self, value: str):
        self._set_element("reponame", value)

    @reponame.deleter
    def reponame(self):
        self._delete_element("reponame")
# {'list': '0+', 'ref': 'architecture-element'}

    _architectures_is_list: bool = True
    _architectures_wrapper_class: Type = Architecture

    @property
    def architectures(self) -> List[Architecture]:
        return self._get_element("architecture", property_name="architectures")

    @architectures.setter
    def architectures(self, value: List[Architecture]):
        self._set_element("architecture", value, property_name="architectures")

    @architectures.deleter
    def architectures(self):
        self._delete_element("architecture", property_name="architectures")
# {'list': '0+', 'ref': 'icon-element'}

    _icons_is_list: bool = True
    _icons_wrapper_class: Type = Icon

    @property
    def icons(self) -> List[Icon]:
        return self._get_element("icon", property_name="icons")

    @icons.setter
    def icons(self, value: List[Icon]):
        self._set_element("icon", value, property_name="icons")

    @icons.deleter
    def icons(self):
        self._delete_element("icon", property_name="icons")
# {}

    @property
    def link(self) -> str:
        return self._get_element("link")

    @link.setter
    def link(self, value: str):
        self._set_element("link", value)

    @link.deleter
    def link(self):
        self._delete_element("link")
