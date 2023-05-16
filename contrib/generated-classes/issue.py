from typing import List
from typing import Type

from . import _base


class Issue(_base.ApiEndPointBase):
    pass

    _elements: List[str] = ['name', 'tracker', 'label', 'url', 'state', 'description', 'owner']
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
    def tracker(self) -> str:
        return self._get_element("tracker")

    @tracker.setter
    def tracker(self, value: str):
        self._set_element("tracker", value)

    @tracker.deleter
    def tracker(self):
        self._delete_element("tracker")
# {'optional': '1'}

    _label_is_optional: bool = True

    @property
    def label(self) -> str:
        return self._get_element("label")

    @label.setter
    def label(self, value: str):
        self._set_element("label", value)

    @label.deleter
    def label(self):
        self._delete_element("label")
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

    _state_is_optional: bool = True

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
# {'optional': '1', 'elements': {'login': {}, 'email': {}, 'realname': {}}}

    _owner_is_optional: bool = True
    _owner_elements: List[str] = ['login', 'email', 'realname']

    @property
    def owner(self) -> str:
        return self._get_element("owner")

    @owner.setter
    def owner(self, value: str):
        self._set_element("owner", value)

    @owner.deleter
    def owner(self):
        self._delete_element("owner")
