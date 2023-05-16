from typing import List
from typing import Type

from . import _base


class Check(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['name', 'required']
    _elements: List[str] = ['state', 'short_description', 'url']

    @property
    def name(self) -> str:
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")

    _required_is_optional: bool = True
    _required_choices: List[str] = ['true', 'false']

    @property
    def required(self) -> str:
        return self._get_attribute("required")

    @required.setter
    def required(self, value: str):
        self._set_attribute("required", value)

    @required.deleter
    def required(self):
        self._delete_attribute("required")
# {'choices': {'values': ['pending', 'error', 'failure', 'success']}}

    _state_choices: List[str] = ['pending', 'error', 'failure', 'success']

    @property
    def state(self) -> str:
        return self._get_element("state")

    @state.setter
    def state(self, value: str):
        self._set_element("state", value)

    @state.deleter
    def state(self):
        self._delete_element("state")
# {'optional': '1'}

    _short_description_is_optional: bool = True

    @property
    def short_description(self) -> str:
        return self._get_element("short_description")

    @short_description.setter
    def short_description(self, value: str):
        self._set_element("short_description", value)

    @short_description.deleter
    def short_description(self):
        self._delete_element("short_description")
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
