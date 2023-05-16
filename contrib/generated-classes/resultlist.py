from typing import List
from typing import Type

from . import _base


class Resultlist(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['state']
    _elements: List[str] = ['result']

    @property
    def state(self) -> str:
        """
        Hash of the returned results.
        """
        return self._get_attribute("state")

    @state.setter
    def state(self, value: str):
        self._set_attribute("state", value)

    @state.deleter
    def state(self):
        self._delete_attribute("state")
# {'doc': 'This element contains the requested build results.\nEach requested repository+architecture combination results in one\nresult element.', 'list': '0+', 'attributes': {'project': {}, 'repository': {}, 'arch': {'doc': 'Build architecture', 'ref': 'build-arch'}, 'state': {'doc': 'Deprecated alias for the code attribute.', 'ref': 'repository-code'}, 'code': {'ref': 'repository-code'}, 'dirty': {'optional': '1', 'doc': 'Specifies whether the repository is currently being recalculated\nand has not "settled" yet.\nDefaults to false and is omitted then.'}}, 'elements': {'status': {'doc': 'One status element is emitted per package (matching the\nrequested filters) if `view=status` was present in the\nparameters to the GET request (or no `view` was specified).', 'list': '0+', 'attributes': {'package': {}, 'code': {'doc': 'The state of the package with the name specified in the\npackage attribute', 'ref': 'package-code'}}, 'elements': {'details': {'doc': "Additional details provided for the package's status,\ne.g. the reason why it failed to resolve.", 'list': '0+'}}}, 'summary': {'optional': '1', 'doc': 'This element is present if `view=summary` is passed as a\nparameter to the GET request.\n\nIt contains one `statuscount` element for each package status\ncode that is present in this repository+architecture\ncombination.', 'elements': {'statuscount': {'doc': 'This element contains the number of packages (in the\n`number` attribute) that have the package code from the\n`code` attribute. Package Codes with no occurrence are\nomitted.', 'list': '0+', 'attributes': {'code': {'ref': 'package-code'}, 'count': {}}}}}, 'binarylist': {'doc': 'This element is present if `view=binarylist` is passed as a\nparameter to the GET request.\nEach element belongs to an individual package (specified via\nthe `package` attribute) and contains the list of the produced\nbinaries as the `binary` child elements.  NOTE: this listing\nwill by default *not* include binaries produced from\nmultibuilds. These have to be explicitly included via the\n`multibuild=1` parameter', 'list': '0+', 'attributes': {'package': {}}, 'elements': {'binary': {'doc': 'Each element corresponds to an individual file that was\nproduced by a package build.', 'list': '0+', 'attributes': {'filename': {}, 'size': {'doc': 'The size of this file in bytes.'}, 'mtime': {'doc': 'Unix time at which this binary was produced.'}}}}}}}

    _results_is_list: bool = True
    _results_attributes: List[str] = ['project', 'repository', 'arch', 'state', 'code', 'dirty']
    _results_elements: List[str] = ['status', 'summary', 'binarylist']

    @property
    def results(self) -> List[str]:
        """
        This element contains the requested build results.
        Each requested repository+architecture combination results in one
        result element.
        """
        return self._get_element("result", property_name="results")

    @results.setter
    def results(self, value: List[str]):
        self._set_element("result", value, property_name="results")

    @results.deleter
    def results(self):
        self._delete_element("result", property_name="results")
