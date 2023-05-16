from typing import List
from typing import Type

from . import _base


class ChannelTarget(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['project', 'repository', 'id_template', 'requires_issue']
    _elements: List[str] = ['disabled']

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

    _id_template_is_optional: bool = True

    @property
    def id_template(self) -> str:
        return self._get_attribute("id_template")

    @id_template.setter
    def id_template(self, value: str):
        self._set_attribute("id_template", value)

    @id_template.deleter
    def id_template(self):
        self._delete_attribute("id_template")

    _requires_issue_is_optional: bool = True

    @property
    def requires_issue(self) -> str:
        return self._get_attribute("requires_issue")

    @requires_issue.setter
    def requires_issue(self, value: str):
        self._set_attribute("requires_issue", value)

    @requires_issue.deleter
    def requires_issue(self):
        self._delete_attribute("requires_issue")
# {'optional': '1', 'doc': 'For disabling the repository. The channel source will be branched but not build enabled by default'}

    _disabled_is_optional: bool = True

    @property
    def disabled(self) -> str:
        """
        For disabling the repository. The channel source will be branched but not build enabled by default
        """
        return self._get_element("disabled")

    @disabled.setter
    def disabled(self, value: str):
        self._set_element("disabled", value)

    @disabled.deleter
    def disabled(self):
        self._delete_element("disabled")
