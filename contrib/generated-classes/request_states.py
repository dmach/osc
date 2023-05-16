from typing import List
from typing import Type

from . import _base


class RequestStates(_base.Choices):
    pass

    _choices: List[str] = ['review', 'new', 'accepted', 'declined', 'revoked', 'superseded', 'deleted']
