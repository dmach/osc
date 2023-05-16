from typing import List
from typing import Type

from . import _base


class PatchinfoCategories(_base.Choices):
    pass

    _choices: List[str] = ['security', 'recommended', 'optional', 'feature', 'ptf']
