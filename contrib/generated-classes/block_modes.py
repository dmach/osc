from typing import List
from typing import Type

from . import _base


class BlockModes(_base.Choices):
    pass

    _choices: List[str] = ['all', 'local', 'never']
