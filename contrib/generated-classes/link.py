from typing import List
from typing import Type

from . import _base
from .patches import Patches


class Link(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['project', 'package', 'missingok', 'rev', 'vrev', 'cicount', 'baserev']
    _elements: List[str] = ['patches']

    _project_is_optional: bool = True

    @property
    def project(self) -> str:
        """
        The name of the project to which this link points.
        """
        return self._get_attribute("project")

    @project.setter
    def project(self, value: str):
        self._set_attribute("project", value)

    @project.deleter
    def project(self):
        self._delete_attribute("project")

    _package_is_optional: bool = True

    @property
    def package(self) -> str:
        """
        The name of the package to which this link points.
        """
        return self._get_attribute("package")

    @package.setter
    def package(self, value: str):
        self._set_attribute("package", value)

    @package.deleter
    def package(self):
        self._delete_attribute("package")

    _missingok_is_optional: bool = True
    _missingok_choices: List[str] = ['true']

    @property
    def missingok(self) -> str:
        """
        Allow linking against packages that have been deleted.

        Choices:
          - ``true``
        """
        return self._get_attribute("missingok")

    @missingok.setter
    def missingok(self, value: str):
        self._set_attribute("missingok", value)

    @missingok.deleter
    def missingok(self):
        self._delete_attribute("missingok")

    _rev_is_optional: bool = True

    @property
    def rev(self) -> str:
        """
        Revision of the package containing the _link file that is used for
        the 3-way merge to construct the expanded sources.
        If omitted, defaults to the latest revision.
        """
        return self._get_attribute("rev")

    @rev.setter
    def rev(self, value: str):
        self._set_attribute("rev", value)

    @rev.deleter
    def rev(self):
        self._delete_attribute("rev")

    _vrev_is_optional: bool = True

    @property
    def vrev(self) -> str:
        return self._get_attribute("vrev")

    @vrev.setter
    def vrev(self, value: str):
        self._set_attribute("vrev", value)

    @vrev.deleter
    def vrev(self):
        self._delete_attribute("vrev")

    _cicount_is_optional: bool = True

    @property
    def cicount(self) -> str:
        """
        Determines how the cicount (=check in count, the number of commits
        since the last version bump of the package) of the linked package is
        calculated.
        If omitted, then the default is "add".
        """
        return self._get_attribute("cicount")

    @cicount.setter
    def cicount(self, value: str):
        self._set_attribute("cicount", value)

    @cicount.deleter
    def cicount(self):
        self._delete_attribute("cicount")

    _baserev_is_optional: bool = True

    @property
    def baserev(self) -> str:
        """
        Revision of the base package to which the link points that is used
        for the 3-way merge to calculate the expanded sources.
        If omitted, then the latest revision is used.
        """
        return self._get_attribute("baserev")

    @baserev.setter
    def baserev(self, value: str):
        self._set_attribute("baserev", value)

    @baserev.deleter
    def baserev(self):
        self._delete_attribute("baserev")
# {'list': '0+', 'ref': 'patches-element'}

    _patchess_is_list: bool = True
    _patchess_wrapper_class: Type = Patches

    @property
    def patchess(self) -> List[Patches]:
        return self._get_element("patches", property_name="patchess")

    @patchess.setter
    def patchess(self, value: List[Patches]):
        self._set_element("patches", value, property_name="patchess")

    @patchess.deleter
    def patchess(self):
        self._delete_element("patches", property_name="patchess")
