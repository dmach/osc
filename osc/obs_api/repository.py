# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional
from typing import Tuple

from . import xmlmodel
from . import choices
from .repository_download import RepositoryDownload
from .repository_hostsystem import RepositoryHostsystem
from .repository_path import RepositoryPath
from .repository_releasetarget import RepositoryReleasetarget


class Repository(xmlmodel.Model):
    TAG_NAME = "repository"

    name: str = xmlmodel.AttributeField(
        "name",
    )

    rebuild: Optional[str] = xmlmodel.AttributeField(
        "rebuild",
        choices=choices.REBUILD_MODES,
        optional=True,
    )

    block: Optional[str] = xmlmodel.AttributeField(
        "block",
        choices=choices.BLOCK_MODES,
        optional=True,
    )

    linkedbuild: Optional[str] = xmlmodel.AttributeField(
        "linkedbuild",
        choices=choices.LINKEDBUILD_MODES,
        optional=True,
    )

    downloads: Optional[Tuple[RepositoryDownload]] = xmlmodel.ModelListField(
        "download",
        model_class=RepositoryDownload,
        optional=True,
    )

    releasetargets: Optional[Tuple[RepositoryReleasetarget]] = xmlmodel.ModelListField(
        "releasetarget",
        model_class=RepositoryReleasetarget,
        optional=True,
    )

    hostsystems: Optional[Tuple[RepositoryHostsystem]] = xmlmodel.ModelListField(
        "hostsystem",
        model_class=RepositoryHostsystem,
        optional=True,
    )

    paths: Optional[Tuple[RepositoryPath]] = xmlmodel.ModelListField(
        "path",
        model_class=RepositoryPath,
        optional=True,
    )

    archs: Optional[Tuple[str]] = xmlmodel.TextNodeListField(
        "arch",
        choices=choices.BUILD_ARCH,
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
