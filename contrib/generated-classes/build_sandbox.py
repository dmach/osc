from typing import List
from typing import Type

from . import _base


class BuildSandbox(_base.Choices):
    pass

    _choices: List[str] = ['chroot', 'lxc', 'kvm', 'xen', 'secure']
