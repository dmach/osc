from typing import List
from typing import Type

from . import _base


class Icon(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['width', 'height', 'url']

    _width_is_optional: bool = True

    @property
    def width(self) -> str:
        return self._get_attribute("width")

    @width.setter
    def width(self, value: str):
        self._set_attribute("width", value)

    @width.deleter
    def width(self):
        self._delete_attribute("width")

    _height_is_optional: bool = True

    @property
    def height(self) -> str:
        return self._get_attribute("height")

    @height.setter
    def height(self, value: str):
        self._set_attribute("height", value)

    @height.deleter
    def height(self):
        self._delete_attribute("height")

    @property
    def url(self) -> str:
        return self._get_attribute("url")

    @url.setter
    def url(self, value: str):
        self._set_attribute("url", value)

    @url.deleter
    def url(self):
        self._delete_attribute("url")
