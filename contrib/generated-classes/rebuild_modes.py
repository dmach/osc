from typing import List
from typing import Type

from . import _base


class RebuildModes(_base.Choices):
    pass

    _choices: List[str] = ['transitive', 'direct', 'local']
