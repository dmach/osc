from typing import List
from typing import Type

from . import _base


class Revisionlist(_base.ApiEndPointBase):
    pass

    _elements: List[str] = ['revision']
# {'doc': 'This element corresponds to a specific revision/commit of this package.', 'list': '0+', 'attributes': {'rev': {'doc': 'Revision number of this commit.'}, 'vrev': {'doc': 'The vrev is maintained by the server and ensures a strictly monotone\nincreasing number for a given version. It consists of the version parsed\nfrom the the build description and the checkin counter. The checkin counter\ngets reset to zero if the new version did not exist yet. Together with the\nbuild counter this forms the version-release of the resulting binary.'}}, 'elements': {'srcmd5': {'doc': 'MD5 hash of this revision as identifier. Note that this is the sum over the\nunexpanded sources (in case a link exists).'}, 'version': {'doc': 'Version (e.g. 1.5.0) of the package at this revision parsed from the source.\nIt may not be set if the package is linking to another package\ninstance. In that case the version will be "unknown".'}, 'time': {'doc': 'Unix timestamp (=seconds since January 1st, 1970 UTC) at which\nthis revision was committed.'}, 'user': {'doc': 'User ID of the user that committed this revision.'}, 'comment': {'optional': '1', 'doc': 'If a comment was added to this revision, then it is displayed here.'}, 'requestid': {'optional': '1', 'doc': "If this revision was created by accepting a request, then the\nrequest's ID is available in this element."}}}

    _revisions_is_list: bool = True
    _revisions_attributes: List[str] = ['rev', 'vrev']
    _revisions_elements: List[str] = ['srcmd5', 'version', 'time', 'user', 'comment', 'requestid']

    @property
    def revisions(self) -> List[str]:
        """
        This element corresponds to a specific revision/commit of this package.
        """
        return self._get_element("revision", property_name="revisions")

    @revisions.setter
    def revisions(self, value: List[str]):
        self._set_element("revision", value, property_name="revisions")

    @revisions.deleter
    def revisions(self):
        self._delete_element("revision", property_name="revisions")
