from typing import List
from typing import Type

from . import _base


class IssueTracker(_base.ApiEndPointBase):
    pass

    _elements: List[str] = ['name', 'label', 'kind', 'description', 'enable-fetch', 'publish-issues', 'issues-updated', 'user', 'password', 'url', 'show-url', 'regex']
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
    def label(self) -> str:
        return self._get_element("label")

    @label.setter
    def label(self, value: str):
        self._set_element("label", value)

    @label.deleter
    def label(self):
        self._delete_element("label")
# {}

    @property
    def kind(self) -> str:
        return self._get_element("kind")

    @kind.setter
    def kind(self, value: str):
        self._set_element("kind", value)

    @kind.deleter
    def kind(self):
        self._delete_element("kind")
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

    _enable_fetch_is_optional: bool = True

    @property
    def enable_fetch(self) -> str:
        return self._get_element("enable-fetch", property_name="enable_fetch")

    @enable_fetch.setter
    def enable_fetch(self, value: str):
        self._set_element("enable-fetch", value, property_name="enable_fetch")

    @enable_fetch.deleter
    def enable_fetch(self):
        self._delete_element("enable-fetch", property_name="enable_fetch")
# {'optional': '1'}

    _publish_issues_is_optional: bool = True

    @property
    def publish_issues(self) -> str:
        return self._get_element("publish-issues", property_name="publish_issues")

    @publish_issues.setter
    def publish_issues(self, value: str):
        self._set_element("publish-issues", value, property_name="publish_issues")

    @publish_issues.deleter
    def publish_issues(self):
        self._delete_element("publish-issues", property_name="publish_issues")
# {'optional': '1'}

    _issues_updated_is_optional: bool = True

    @property
    def issues_updated(self) -> str:
        return self._get_element("issues-updated", property_name="issues_updated")

    @issues_updated.setter
    def issues_updated(self, value: str):
        self._set_element("issues-updated", value, property_name="issues_updated")

    @issues_updated.deleter
    def issues_updated(self):
        self._delete_element("issues-updated", property_name="issues_updated")
# {'optional': '1'}

    _user_is_optional: bool = True

    @property
    def user(self) -> str:
        return self._get_element("user")

    @user.setter
    def user(self, value: str):
        self._set_element("user", value)

    @user.deleter
    def user(self):
        self._delete_element("user")
# {'optional': '1'}

    _password_is_optional: bool = True

    @property
    def password(self) -> str:
        return self._get_element("password")

    @password.setter
    def password(self, value: str):
        self._set_element("password", value)

    @password.deleter
    def password(self):
        self._delete_element("password")
# {}

    @property
    def url(self) -> str:
        return self._get_element("url")

    @url.setter
    def url(self, value: str):
        self._set_element("url", value)

    @url.deleter
    def url(self):
        self._delete_element("url")
# {}

    @property
    def show_url(self) -> str:
        return self._get_element("show-url", property_name="show_url")

    @show_url.setter
    def show_url(self, value: str):
        self._set_element("show-url", value, property_name="show_url")

    @show_url.deleter
    def show_url(self):
        self._delete_element("show-url", property_name="show_url")
# {}

    @property
    def regex(self) -> str:
        return self._get_element("regex")

    @regex.setter
    def regex(self, value: str):
        self._set_element("regex", value)

    @regex.deleter
    def regex(self):
        self._delete_element("regex")
