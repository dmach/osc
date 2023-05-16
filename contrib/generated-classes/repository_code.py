from typing import List
from typing import Type

from . import _base


class RepositoryCode(_base.Choices):
    pass

    _choices: List[str] = ['unknown', 'broken', 'scheduling', 'blocked', 'building', 'finished', 'publishing', 'published', 'unpublished']
