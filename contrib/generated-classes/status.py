from typing import List
from typing import Type

from . import _base


class Status(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['package', 'code', 'dirty']
    _elements: List[str] = ['details']

    @property
    def package(self) -> str:
        return self._get_attribute("package")

    @package.setter
    def package(self, value: str):
        self._set_attribute("package", value)

    @package.deleter
    def package(self):
        self._delete_attribute("package")

    @property
    def code(self) -> str:
        return self._get_attribute("code")

    @code.setter
    def code(self, value: str):
        self._set_attribute("code", value)

    @code.deleter
    def code(self):
        self._delete_attribute("code")

    _dirty_is_optional: bool = True

    @property
    def dirty(self) -> str:
        """
        Defaults to false and is omitted then.
        """
        return self._get_attribute("dirty")

    @dirty.setter
    def dirty(self, value: str):
        self._set_attribute("dirty", value)

    @dirty.deleter
    def dirty(self):
        self._delete_attribute("dirty")
# {'optional': '1', 'doc': 'Optionally this element contains additional information about the\ncurrent state of the build (e.g. on which worker it is being built)'}

    _details_is_optional: bool = True

    @property
    def details(self) -> str:
        """
        Optionally this element contains additional information about the
        current state of the build (e.g. on which worker it is being built)
        """
        return self._get_element("details")

    @details.setter
    def details(self, value: str):
        self._set_element("details", value)

    @details.deleter
    def details(self):
        self._delete_element("details")
