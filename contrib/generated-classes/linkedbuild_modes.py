from typing import List
from typing import Type

from . import _base


class LinkedbuildModes(_base.Choices):
    pass

    _choices: List[str] = ['off', 'localdep', 'alldirect', 'all']
