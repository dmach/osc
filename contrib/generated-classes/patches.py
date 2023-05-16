from typing import List
from typing import Type

from . import _base


class Patches(_base.ApiEndPointBase):
    pass

    _elements: List[str] = ['add', 'apply', 'delete', 'branch', 'topadd']
# {'doc': 'Add a file to the package on top of the original package.', 'list': '0+', 'attributes': {'name': {'doc': 'Name of the file which should be added to the package. It must\nbe checked-in in the unexpanded package.'}, 'type': {'optional': '1'}, 'after': {'optional': '1'}, 'popt': {'optional': '1'}, 'dir': {'optional': '1'}}}

    _adds_is_list: bool = True
    _adds_attributes: List[str] = ['name', 'type', 'after', 'popt', 'dir']

    @property
    def adds(self) -> List[str]:
        """
        Add a file to the package on top of the original package.
        """
        return self._get_element("add", property_name="adds")

    @adds.setter
    def adds(self, value: List[str]):
        self._set_element("add", value, property_name="adds")

    @adds.deleter
    def adds(self):
        self._delete_element("add", property_name="adds")
# {'doc': 'Apply the patch with the supplied name when expanding the sources.', 'list': '0+', 'attributes': {'name': {}}}

    _applies_is_list: bool = True
    _applies_attributes: List[str] = ['name']

    @property
    def applies(self) -> List[str]:
        """
        Apply the patch with the supplied name when expanding the sources.
        """
        return self._get_element("apply", property_name="applies")

    @applies.setter
    def applies(self, value: List[str]):
        self._set_element("apply", value, property_name="applies")

    @applies.deleter
    def applies(self):
        self._delete_element("apply", property_name="applies")
# {'doc': 'Remove the file with the supplied name when expanding the sources.', 'list': '0+', 'attributes': {'name': {}}}

    _deletes_is_list: bool = True
    _deletes_attributes: List[str] = ['name']

    @property
    def deletes(self) -> List[str]:
        """
        Remove the file with the supplied name when expanding the sources.
        """
        return self._get_element("delete", property_name="deletes")

    @deletes.setter
    def deletes(self, value: List[str]):
        self._set_element("delete", value, property_name="deletes")

    @deletes.deleter
    def deletes(self):
        self._delete_element("delete", property_name="deletes")
# {'optional': '1', 'doc': 'If present, then perform a full copy of all sources from the link\nsource into the current package.'}

    _branch_is_optional: bool = True

    @property
    def branch(self) -> str:
        """
        If present, then perform a full copy of all sources from the link
        source into the current package.
        """
        return self._get_element("branch")

    @branch.setter
    def branch(self, value: str):
        self._set_element("branch", value)

    @branch.deleter
    def branch(self):
        self._delete_element("branch")
# {'doc': 'Add the given string to the top of the spec file in the package sources.', 'list': '0+'}

    _topadds_is_list: bool = True

    @property
    def topadds(self) -> List[str]:
        """
        Add the given string to the top of the spec file in the package sources.
        """
        return self._get_element("topadd", property_name="topadds")

    @topadds.setter
    def topadds(self, value: List[str]):
        self._set_element("topadd", value, property_name="topadds")

    @topadds.deleter
    def topadds(self):
        self._delete_element("topadd", property_name="topadds")
