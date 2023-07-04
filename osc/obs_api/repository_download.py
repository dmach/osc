# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional

from . import xmlmodel
from .repository_master import RepositoryMaster


class RepositoryDownload(xmlmodel.Model):
    TAG_NAME = "download"

    arch: str = xmlmodel.AttributeField(
        "arch",
    )

    url: str = xmlmodel.AttributeField(
        "url",
    )

    repotype: str = xmlmodel.AttributeField(
        "repotype",
        choices=('rpmmd', 'susetags', 'deb', 'arch', 'mdk', 'registry'),
    )

    archfilter: Optional[str] = xmlmodel.TextNodeField(
        "archfilter",
        optional=True,
    )

    master: Optional[RepositoryMaster] = xmlmodel.ModelField(
        "master",
        model_class=RepositoryMaster,
        optional=True,
    )

    pubkey: Optional[str] = xmlmodel.TextNodeField(
        "pubkey",
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
