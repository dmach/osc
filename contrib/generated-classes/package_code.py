from typing import List
from typing import Type

from . import _base


class PackageCode(_base.Choices):
    pass

    _choices: List[str] = ['unresolvable', 'succeeded', 'failed', 'broken', 'disabled', 'excluded', 'blocked', 'locked', 'unknown', 'scheduled', 'building', 'finished']
