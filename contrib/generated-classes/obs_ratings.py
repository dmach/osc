from typing import List
from typing import Type

from . import _base


class ObsRatings(_base.Choices):
    pass

    _choices: List[str] = ['low', 'moderate', 'important', 'critical']
