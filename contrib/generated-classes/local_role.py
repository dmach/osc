from typing import List
from typing import Type

from . import _base


class LocalRole(_base.Choices):
    pass

    _choices: List[str] = ['maintainer', 'bugowner', 'reviewer', 'downloader', 'reader']
