from typing import List
from typing import Type

from . import _base


class Cicount(_base.Choices):
    pass

    _choices: List[str] = ['add', 'copy', 'local']
