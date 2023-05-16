from typing import List
from typing import Type

from . import _base


class AttributeKind(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['kind']

    _kind_choices: List[str] = ['package', 'patch', 'script', 'message', 'product', 'atom']

    @property
    def kind(self) -> str:
        return self._get_attribute("kind")

    @kind.setter
    def kind(self, value: str):
        self._set_attribute("kind", value)

    @kind.deleter
    def kind(self):
        self._delete_attribute("kind")
