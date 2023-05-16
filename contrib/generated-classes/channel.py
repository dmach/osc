from typing import List
from typing import Type

from . import _base
from .channel_binaries import ChannelBinaries
from .channel_product import ChannelProduct
from .channel_target import ChannelTarget


class Channel(_base.ApiEndPointBase):
    pass

    _elements: List[str] = ['disabled', 'product', 'target', 'binaries']
# {'optional': '1', 'doc': "For disabling the entire channel. The channel source won't be branched by default"}

    _disabled_is_optional: bool = True

    @property
    def disabled(self) -> str:
        """
        For disabling the entire channel. The channel source won't be branched by default
        """
        return self._get_element("disabled")

    @disabled.setter
    def disabled(self, value: str):
        self._set_element("disabled", value)

    @disabled.deleter
    def disabled(self):
        self._delete_element("disabled")
# {'list': '0+', 'ref': 'channel-product-element'}

    _products_is_list: bool = True
    _products_wrapper_class: Type = ChannelProduct

    @property
    def products(self) -> List[ChannelProduct]:
        return self._get_element("product", property_name="products")

    @products.setter
    def products(self, value: List[ChannelProduct]):
        self._set_element("product", value, property_name="products")

    @products.deleter
    def products(self):
        self._delete_element("product", property_name="products")
# {'list': '0+', 'ref': 'channel-target-element'}

    _targets_is_list: bool = True
    _targets_wrapper_class: Type = ChannelTarget

    @property
    def targets(self) -> List[ChannelTarget]:
        return self._get_element("target", property_name="targets")

    @targets.setter
    def targets(self, value: List[ChannelTarget]):
        self._set_element("target", value, property_name="targets")

    @targets.deleter
    def targets(self):
        self._delete_element("target", property_name="targets")
# {'list': '1+', 'ref': 'channel-binaries-element'}

    _binariess_is_list: bool = True
    _binariess_wrapper_class: Type = ChannelBinaries

    @property
    def binariess(self) -> List[ChannelBinaries]:
        return self._get_element("binaries", property_name="binariess")

    @binariess.setter
    def binariess(self, value: List[ChannelBinaries]):
        self._set_element("binaries", value, property_name="binariess")

    @binariess.deleter
    def binariess(self):
        self._delete_element("binaries", property_name="binariess")
