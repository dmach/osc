from typing import List
from typing import Type

from . import _base
from .issue import Issue
from .obs_ratings import ObsRatings
from .patchinfo_categories import PatchinfoCategories


class Patchinfo(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['incident', 'version']
    _elements: List[str] = ['releasetarget', 'package', 'binary', 'issue', 'name', 'category', 'rating', 'summary', 'description', 'message', 'packager', 'stopped', 'retracted', 'reboot_needed', 'relogin_needed', 'zypp_restart_needed']

    _incident_is_optional: bool = True

    @property
    def incident(self) -> str:
        return self._get_attribute("incident")

    @incident.setter
    def incident(self, value: str):
        self._set_attribute("incident", value)

    @incident.deleter
    def incident(self):
        self._delete_attribute("incident")

    _version_is_optional: bool = True

    @property
    def version(self) -> str:
        return self._get_attribute("version")

    @version.setter
    def version(self, value: str):
        self._set_attribute("version", value)

    @version.deleter
    def version(self):
        self._delete_attribute("version")
# {'list': '0+', 'attributes': {'project': {}, 'repository': {'optional': '1'}}}

    _releasetargets_is_list: bool = True
    _releasetargets_attributes: List[str] = ['project', 'repository']

    @property
    def releasetargets(self) -> List[str]:
        return self._get_element("releasetarget", property_name="releasetargets")

    @releasetargets.setter
    def releasetargets(self, value: List[str]):
        self._set_element("releasetarget", value, property_name="releasetargets")

    @releasetargets.deleter
    def releasetargets(self):
        self._delete_element("releasetarget", property_name="releasetargets")
# {'list': '0+'}

    _packages_is_list: bool = True

    @property
    def packages(self) -> List[str]:
        return self._get_element("package", property_name="packages")

    @packages.setter
    def packages(self, value: List[str]):
        self._set_element("package", value, property_name="packages")

    @packages.deleter
    def packages(self):
        self._delete_element("package", property_name="packages")
# {'list': '0+'}

    _binaries_is_list: bool = True

    @property
    def binaries(self) -> List[str]:
        return self._get_element("binary", property_name="binaries")

    @binaries.setter
    def binaries(self, value: List[str]):
        self._set_element("binary", value, property_name="binaries")

    @binaries.deleter
    def binaries(self):
        self._delete_element("binary", property_name="binaries")
# {'list': '0+', 'ref': 'issue-element'}

    _issues_is_list: bool = True
    _issues_wrapper_class: Type = Issue

    @property
    def issues(self) -> List[Issue]:
        return self._get_element("issue", property_name="issues")

    @issues.setter
    def issues(self, value: List[Issue]):
        self._set_element("issue", value, property_name="issues")

    @issues.deleter
    def issues(self):
        self._delete_element("issue", property_name="issues")
# {'optional': '1'}

    _name_is_optional: bool = True

    @property
    def name(self) -> str:
        return self._get_element("name")

    @name.setter
    def name(self, value: str):
        self._set_element("name", value)

    @name.deleter
    def name(self):
        self._delete_element("name")
# {'ref': 'patchinfo-categories'}

    _category_wrapper_class: Type = PatchinfoCategories

    @property
    def category(self) -> PatchinfoCategories:
        return self._get_element("category")

    @category.setter
    def category(self, value: PatchinfoCategories):
        self._set_element("category", value)

    @category.deleter
    def category(self):
        self._delete_element("category")
# {'ref': 'obs-ratings'}

    _rating_wrapper_class: Type = ObsRatings

    @property
    def rating(self) -> ObsRatings:
        return self._get_element("rating")

    @rating.setter
    def rating(self, value: ObsRatings):
        self._set_element("rating", value)

    @rating.deleter
    def rating(self):
        self._delete_element("rating")
# {}

    @property
    def summary(self) -> str:
        return self._get_element("summary")

    @summary.setter
    def summary(self, value: str):
        self._set_element("summary", value)

    @summary.deleter
    def summary(self):
        self._delete_element("summary")
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

    _message_is_optional: bool = True

    @property
    def message(self) -> str:
        return self._get_element("message")

    @message.setter
    def message(self, value: str):
        self._set_element("message", value)

    @message.deleter
    def message(self):
        self._delete_element("message")
# {}

    @property
    def packager(self) -> str:
        return self._get_element("packager")

    @packager.setter
    def packager(self, value: str):
        self._set_element("packager", value)

    @packager.deleter
    def packager(self):
        self._delete_element("packager")
# {'optional': '1'}

    _stopped_is_optional: bool = True

    @property
    def stopped(self) -> str:
        return self._get_element("stopped")

    @stopped.setter
    def stopped(self, value: str):
        self._set_element("stopped", value)

    @stopped.deleter
    def stopped(self):
        self._delete_element("stopped")
# {'optional': '1'}

    _retracted_is_optional: bool = True

    @property
    def retracted(self) -> str:
        return self._get_element("retracted")

    @retracted.setter
    def retracted(self, value: str):
        self._set_element("retracted", value)

    @retracted.deleter
    def retracted(self):
        self._delete_element("retracted")
# {'optional': '1'}

    _reboot_needed_is_optional: bool = True

    @property
    def reboot_needed(self) -> str:
        return self._get_element("reboot_needed")

    @reboot_needed.setter
    def reboot_needed(self, value: str):
        self._set_element("reboot_needed", value)

    @reboot_needed.deleter
    def reboot_needed(self):
        self._delete_element("reboot_needed")
# {'optional': '1'}

    _relogin_needed_is_optional: bool = True

    @property
    def relogin_needed(self) -> str:
        return self._get_element("relogin_needed")

    @relogin_needed.setter
    def relogin_needed(self, value: str):
        self._set_element("relogin_needed", value)

    @relogin_needed.deleter
    def relogin_needed(self):
        self._delete_element("relogin_needed")
# {'optional': '1'}

    _zypp_restart_needed_is_optional: bool = True

    @property
    def zypp_restart_needed(self) -> str:
        return self._get_element("zypp_restart_needed")

    @zypp_restart_needed.setter
    def zypp_restart_needed(self, value: str):
        self._set_element("zypp_restart_needed", value)

    @zypp_restart_needed.deleter
    def zypp_restart_needed(self):
        self._delete_element("zypp_restart_needed")
