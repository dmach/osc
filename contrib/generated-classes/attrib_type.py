from typing import List
from typing import Type

from . import _base


class Attrib_type(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['namespace', 'name']
    _elements: List[str] = ['count', 'description', 'default', 'allowed', 'issue_list', 'modifiable_by']

    @property
    def namespace(self) -> str:
        return self._get_attribute("namespace")

    @namespace.setter
    def namespace(self, value: str):
        self._set_attribute("namespace", value)

    @namespace.deleter
    def namespace(self):
        self._delete_attribute("namespace")

    @property
    def name(self) -> str:
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")
# {'optional': '1'}

    _count_is_optional: bool = True

    @property
    def count(self) -> str:
        return self._get_element("count")

    @count.setter
    def count(self, value: str):
        self._set_element("count", value)

    @count.deleter
    def count(self):
        self._delete_element("count")
# {'optional': '1'}

    _description_is_optional: bool = True

    @property
    def description(self) -> str:
        return self._get_element("description")

    @description.setter
    def description(self, value: str):
        self._set_element("description", value)

    @description.deleter
    def description(self):
        self._delete_element("description")
# {'optional': '1', 'elements': {'value': {'list': '0+', 'ref': 'attrib_type_value-element'}}}

    _default_is_optional: bool = True
    _default_elements: List[str] = ['value']

    @property
    def default(self) -> str:
        return self._get_element("default")

    @default.setter
    def default(self, value: str):
        self._set_element("default", value)

    @default.deleter
    def default(self):
        self._delete_element("default")
# {'optional': '1', 'elements': {'value': {'list': '0+', 'ref': 'attrib_type_value-element'}}}

    _allowed_is_optional: bool = True
    _allowed_elements: List[str] = ['value']

    @property
    def allowed(self) -> str:
        return self._get_element("allowed")

    @allowed.setter
    def allowed(self, value: str):
        self._set_element("allowed", value)

    @allowed.deleter
    def allowed(self):
        self._delete_element("allowed")
# {'optional': '1'}

    _issue_list_is_optional: bool = True

    @property
    def issue_list(self) -> str:
        return self._get_element("issue_list")

    @issue_list.setter
    def issue_list(self, value: str):
        self._set_element("issue_list", value)

    @issue_list.deleter
    def issue_list(self):
        self._delete_element("issue_list")
# {'list': '0+', 'attributes': {'user': {'optional': '1'}, 'group': {'optional': '1'}, 'role': {'optional': '1', 'ref': 'local-role'}}}

    _modifiable_bies_is_list: bool = True
    _modifiable_bies_attributes: List[str] = ['user', 'group', 'role']

    @property
    def modifiable_bies(self) -> List[str]:
        return self._get_element("modifiable_by", property_name="modifiable_bies")

    @modifiable_bies.setter
    def modifiable_bies(self, value: List[str]):
        self._set_element("modifiable_by", value, property_name="modifiable_bies")

    @modifiable_bies.deleter
    def modifiable_bies(self):
        self._delete_element("modifiable_by", property_name="modifiable_bies")
