from . import xmlmodel
from .repository_master import RepositoryMaster


class RepositoryDownload(xmlmodel.Model):
    TAG_NAME = "download"

    arch = xmlmodel.AttributeField(
        "arch",
    )

    url = xmlmodel.AttributeField(
        "url",
    )

    repotype = xmlmodel.AttributeField(
        "repotype",
        choices=('rpmmd', 'susetags', 'deb', 'arch', 'mdk', 'registry'),
    )

    archfilter = xmlmodel.TextNodeField(
        "archfilter",
        optional=True,
    )

    master = xmlmodel.ModelField(
        "master",
        model_class=RepositoryMaster,
        optional=True,
    )

    pubkey = xmlmodel.TextNodeField(
        "pubkey",
        optional=True,
    )
