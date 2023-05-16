from typing import List
from typing import Type

from . import _base
from .issue_tracker import IssueTracker


class IssueTrackers(_base.ApiEndPointBase):
    pass

    _elements: List[str] = ['issue-tracker']
# {'list': '0+', 'ref': 'issue-tracker-element'}

    _issue_trackers_is_list: bool = True
    _issue_trackers_wrapper_class: Type = IssueTracker

    @property
    def issue_trackers(self) -> List[IssueTracker]:
        return self._get_element("issue-tracker", property_name="issue_trackers")

    @issue_trackers.setter
    def issue_trackers(self, value: List[IssueTracker]):
        self._set_element("issue-tracker", value, property_name="issue_trackers")

    @issue_trackers.deleter
    def issue_trackers(self):
        self._delete_element("issue-tracker", property_name="issue_trackers")
