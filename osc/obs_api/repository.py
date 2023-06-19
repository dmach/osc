from . import xmlmodel
from . import choices
from .repository_download import RepositoryDownload
from .repository_hostsystem import RepositoryHostsystem
from .repository_path import RepositoryPath
from .repository_releasetarget import RepositoryReleasetarget


class Repository(xmlmodel.Model):
    TAG_NAME = "repository"

    name = xmlmodel.AttributeField(
        "name",
    )

    rebuild = xmlmodel.AttributeField(
        "rebuild",
        choices=choices.REBUILD_MODES,
        optional=True,
    )

    block = xmlmodel.AttributeField(
        "block",
        choices=choices.BLOCK_MODES,
        optional=True,
    )

    linkedbuild = xmlmodel.AttributeField(
        "linkedbuild",
        choices=choices.LINKEDBUILD_MODES,
        optional=True,
    )

    downloads = xmlmodel.ModelListField(
        "download",
        model_class=RepositoryDownload,
        optional=True,
    )

    releasetargets = xmlmodel.ModelListField(
        "releasetarget",
        model_class=RepositoryReleasetarget,
        optional=True,
    )

    hostsystems = xmlmodel.ModelListField(
        "hostsystem",
        model_class=RepositoryHostsystem,
        optional=True,
    )

    paths = xmlmodel.ModelListField(
        "path",
        model_class=RepositoryPath,
        optional=True,
    )

    archs = xmlmodel.TextNodeListField(
        "arch",
        choices=choices.BUILD_ARCH,
        optional=True,
    )
