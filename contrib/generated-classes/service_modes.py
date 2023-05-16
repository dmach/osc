from typing import List
from typing import Type

from . import _base


class ServiceModes(_base.Choices):
    pass

    _choices: List[str] = ['trylocal', 'localonly', 'serveronly', 'buildtime', 'manual', 'disabled']
