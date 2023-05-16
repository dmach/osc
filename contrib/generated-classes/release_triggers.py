from typing import List
from typing import Type

from . import _base


class ReleaseTriggers(_base.Choices):
    pass

    _choices: List[str] = ['manual', 'maintenance', 'obsgendiff']
