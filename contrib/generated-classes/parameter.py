from typing import List
from typing import Type

from . import _base


class Parameter(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['name']
    _elements: List[str] = ['description', 'required', 'allowmultiple', 'allowedvalue']

    @property
    def name(self) -> str:
        """
        Parameter name for the service executable. Can be any, except "outdir" which
        exists always implicit.
        """
        return self._get_attribute("name")

    @name.setter
    def name(self, value: str):
        self._set_attribute("name", value)

    @name.deleter
    def name(self):
        self._delete_attribute("name")
# {'doc': 'Description for the (not anymore existing) webui service editor.'}

    @property
    def description(self) -> str:
        """
        Description for the (not anymore existing) webui service editor.
        """
        return self._get_element("description")

    @description.setter
    def description(self, value: str):
        self._set_element("description", value)

    @description.deleter
    def description(self):
        self._delete_element("description")
# {'optional': '1', 'doc': 'Parameters are optional by default, this is a marker to make it required.\nA hint for the UI.'}

    _required_is_optional: bool = True

    @property
    def required(self) -> str:
        """
        Parameters are optional by default, this is a marker to make it required.
        A hint for the UI.
        """
        return self._get_element("required")

    @required.setter
    def required(self, value: str):
        self._set_element("required", value)

    @required.deleter
    def required(self):
        self._delete_element("required")
# {'optional': '1', 'doc': 'This parameter can be used multiple times.\nA hint for the UI.'}

    _allowmultiple_is_optional: bool = True

    @property
    def allowmultiple(self) -> str:
        """
        This parameter can be used multiple times.
        A hint for the UI.
        """
        return self._get_element("allowmultiple")

    @allowmultiple.setter
    def allowmultiple(self, value: str):
        self._set_element("allowmultiple", value)

    @allowmultiple.deleter
    def allowmultiple(self):
        self._delete_element("allowmultiple")
# {'doc': 'Allowed values for the parameter.\nA hint for the UI to offer a selector.', 'list': '0+'}

    _allowedvalues_is_list: bool = True

    @property
    def allowedvalues(self) -> List[str]:
        """
        Allowed values for the parameter.
        A hint for the UI to offer a selector.
        """
        return self._get_element("allowedvalue", property_name="allowedvalues")

    @allowedvalues.setter
    def allowedvalues(self, value: List[str]):
        self._set_element("allowedvalue", value, property_name="allowedvalues")

    @allowedvalues.deleter
    def allowedvalues(self):
        self._delete_element("allowedvalue", property_name="allowedvalues")
