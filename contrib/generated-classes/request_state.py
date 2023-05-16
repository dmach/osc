from typing import List
from typing import Type

from . import _base


class RequestState(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['name', 'who', 'when', 'created', 'superseded_by', 'approver']
    _elements: List[str] = ['comment']

    @property
    def name(self) -> str:
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")

    _who_is_optional: bool = True

    @property
    def who(self) -> str:
        return self._get_attribute("who")

    @who.setter
    def who(self, value: str):
        self._set_attribute("who", value)

    @who.deleter
    def who(self):
        self._delete_attribute("who")

    _when_is_optional: bool = True

    @property
    def when(self) -> str:
        return self._get_attribute("when")

    @when.setter
    def when(self, value: str):
        self._set_attribute("when", value)

    @when.deleter
    def when(self):
        self._delete_attribute("when")

    _created_is_optional: bool = True

    @property
    def created(self) -> str:
        return self._get_attribute("created")

    @created.setter
    def created(self, value: str):
        self._set_attribute("created", value)

    @created.deleter
    def created(self):
        self._delete_attribute("created")

    _superseded_by_is_optional: bool = True

    @property
    def superseded_by(self) -> str:
        return self._get_attribute("superseded_by")

    @superseded_by.setter
    def superseded_by(self, value: str):
        self._set_attribute("superseded_by", value)

    @superseded_by.deleter
    def superseded_by(self):
        self._delete_attribute("superseded_by")

    _approver_is_optional: bool = True

    @property
    def approver(self) -> str:
        return self._get_attribute("approver")

    @approver.setter
    def approver(self, value: str):
        self._set_attribute("approver", value)

    @approver.deleter
    def approver(self):
        self._delete_attribute("approver")
# {'optional': '1'}

    _comment_is_optional: bool = True

    @property
    def comment(self) -> str:
        return self._get_element("comment")

    @comment.setter
    def comment(self, value: str):
        self._set_element("comment", value)

    @comment.deleter
    def comment(self):
        self._delete_element("comment")
