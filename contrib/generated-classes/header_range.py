from typing import List
from typing import Type

from . import _base


class HeaderRange(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['start', 'end']

    @property
    def start(self) -> str:
        return self._get_attribute("start")

    @start.setter
    def start(self, value: str):
        self._set_attribute("start", value)

    @start.deleter
    def start(self):
        self._delete_attribute("start")

    @property
    def end(self) -> str:
        return self._get_attribute("end")

    @end.setter
    def end(self, value: str):
        self._set_attribute("end", value)

    @end.deleter
    def end(self):
        self._delete_attribute("end")
