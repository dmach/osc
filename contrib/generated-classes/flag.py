from typing import List
from typing import Type

from . import _base


class Flag(_base.ElementChoices):
    pass

    _elements: List[str] = ['enable', 'disable']
