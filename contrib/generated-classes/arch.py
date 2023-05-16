from typing import List
from typing import Type

from . import _base


class Arch(_base.Choices):
    pass

    _choices: List[str] = ['noarch', 'athlon', 'i386', 'i486', 'i586', 'i686', 'ia64', 'ppc', 'ppc64', 's390', 's390x', 'x86_64', 'src']
