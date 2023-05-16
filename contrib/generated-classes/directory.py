from typing import List
from typing import Type

from . import _base


class Directory(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['count']
    _elements: List[str] = ['entry']

    @property
    def count(self) -> str:
        """
        Total number of tokens returned by this query.
        """
        return self._get_attribute("count")

    @count.setter
    def count(self, value: str):
        self._set_attribute("count", value)

    @count.deleter
    def count(self):
        self._delete_attribute("count")
# {'doc': 'Each entry corresponds to a individual token. Each token is identified by\nits id attribute.', 'list': '0+', 'attributes': {'id': {'doc': 'The unique id of this token.'}, 'string': {'doc': 'The token secret. This string can be used instead of the password to\nauthenticate the user or to trigger service runs via the\n`POST /trigger/runservice` route.'}, 'name': {'optional': '1', 'doc': 'This attribute can be used to identify a token from the list of tokens\nof a user.'}, 'project': {'optional': '1', 'doc': "If this token is bound to a specific package, then the packages'\nproject is available in this attribute."}, 'package': {'optional': '1', 'doc': 'The package name to which this token is bound, if it has been created\nfor a specific package. Otherwise this attribute and the project\nattribute are omitted.'}, 'kind': {'doc': 'This attribute specifies which actions can be performed via this token.\n- rss: used to retrieve the notification RSS feed\n- rebuild: trigger rebuilds of packages\n- release: trigger project releases\n- runservice: run a service via the POST /trigger/runservice route', 'ref': 'token-kind'}, 'triggered_at': {'doc': 'The date and time a token got triggered the last time.'}}}

    _entries_is_list: bool = True
    _entries_attributes: List[str] = ['id', 'string', 'name', 'project', 'package', 'kind', 'triggered_at']

    @property
    def entries(self) -> List[str]:
        """
        Each entry corresponds to a individual token. Each token is identified by
        its id attribute.
        """
        return self._get_element("entry", property_name="entries")

    @entries.setter
    def entries(self, value: List[str]):
        self._set_element("entry", value, property_name="entries")

    @entries.deleter
    def entries(self):
        self._delete_element("entry", property_name="entries")
