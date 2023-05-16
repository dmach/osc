from typing import List
from typing import Type

from . import _base


class Multibuild(_base.ElementChoices):
    pass

    _elements: List[str] = ['flavor', 'package']
