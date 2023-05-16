from typing import List
from typing import Type

from . import _base


class GlobalRole(_base.Choices):
    pass

    _choices: List[str] = ['Admin', 'User']
