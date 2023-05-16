from typing import List
from typing import Type

from . import _base


class JobstatusResult(_base.Choices):
    pass

    _choices: List[str] = ['succeeded', 'failed', 'unchanged']
