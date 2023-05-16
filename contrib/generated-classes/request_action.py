from typing import List
from typing import Type

from . import _base


class RequestAction(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['type']
    _elements: List[str] = ['source', 'target', 'person', 'group', 'grouped', 'options', 'acceptinfo']

    _type_choices: List[str] = ['submit', 'delete', 'change_devel', 'add_role', 'set_bugowner', 'maintenance_incident', 'maintenance_release', 'release', 'group']

    @property
    def type(self) -> str:
        return self._get_attribute("type")

    @type.setter
    def type(self, value: str):
        self._set_attribute("type", value)

    @type.deleter
    def type(self):
        self._delete_attribute("type")
# {'optional': '1', 'attributes': {'project': {}, 'package': {'optional': '1'}, 'rev': {'optional': '1'}}}

    _source_is_optional: bool = True
    _source_attributes: List[str] = ['project', 'package', 'rev']

    @property
    def source(self) -> str:
        return self._get_element("source")

    @source.setter
    def source(self, value: str):
        self._set_element("source", value)

    @source.deleter
    def source(self):
        self._delete_element("source")
# {'optional': '1', 'attributes': {'project': {}, 'package': {'optional': '1'}, 'releaseproject': {'optional': '1'}, 'repository': {'optional': '1'}}}

    _target_is_optional: bool = True
    _target_attributes: List[str] = ['project', 'package', 'releaseproject', 'repository']

    @property
    def target(self) -> str:
        return self._get_element("target")

    @target.setter
    def target(self, value: str):
        self._set_element("target", value)

    @target.deleter
    def target(self):
        self._delete_element("target")
# {'optional': '1', 'attributes': {'name': {}, 'role': {'optional': '1'}}}

    _person_is_optional: bool = True
    _person_attributes: List[str] = ['name', 'role']

    @property
    def person(self) -> str:
        return self._get_element("person")

    @person.setter
    def person(self, value: str):
        self._set_element("person", value)

    @person.deleter
    def person(self):
        self._delete_element("person")
# {'optional': '1', 'attributes': {'name': {}, 'role': {'optional': '1'}}}

    _group_is_optional: bool = True
    _group_attributes: List[str] = ['name', 'role']

    @property
    def group(self) -> str:
        return self._get_element("group")

    @group.setter
    def group(self, value: str):
        self._set_element("group", value)

    @group.deleter
    def group(self):
        self._delete_element("group")
# {'optional': '1', 'list': '1+', 'attributes': {'id': {}}}

    _groupeds_is_list: bool = True
    _groupeds_is_optional: bool = True
    _groupeds_attributes: List[str] = ['id']

    @property
    def groupeds(self) -> List[str]:
        return self._get_element("grouped", property_name="groupeds")

    @groupeds.setter
    def groupeds(self, value: List[str]):
        self._set_element("grouped", value, property_name="groupeds")

    @groupeds.deleter
    def groupeds(self):
        self._delete_element("grouped", property_name="groupeds")
# {'optional': '1', 'elements': {'sourceupdate': {'optional': '1', 'choices': {'values': ['update', 'noupdate', 'cleanup']}}, 'updatelink': {'optional': '1', 'choices': {'values': ['true', 'false']}}, 'makeoriginolder': {'optional': '1', 'choices': {'values': ['true', 'false']}}}}

    _options_is_optional: bool = True
    _options_elements: List[str] = ['sourceupdate', 'updatelink', 'makeoriginolder']

    @property
    def options(self) -> str:
        return self._get_element("options")

    @options.setter
    def options(self, value: str):
        self._set_element("options", value)

    @options.deleter
    def options(self):
        self._delete_element("options")
# {'optional': '1', 'attributes': {'rev': {}, 'srcmd5': {}, 'osrcmd5': {}, 'oproject': {'optional': '1'}, 'opackage': {'optional': '1'}, 'xsrcmd5': {'optional': '1'}, 'oxsrcmd5': {'optional': '1'}}}

    _acceptinfo_is_optional: bool = True
    _acceptinfo_attributes: List[str] = ['rev', 'srcmd5', 'osrcmd5', 'oproject', 'opackage', 'xsrcmd5', 'oxsrcmd5']

    @property
    def acceptinfo(self) -> str:
        return self._get_element("acceptinfo")

    @acceptinfo.setter
    def acceptinfo(self, value: str):
        self._set_element("acceptinfo", value)

    @acceptinfo.deleter
    def acceptinfo(self):
        self._delete_element("acceptinfo")
