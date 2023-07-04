# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional

from . import xmlmodel


class RepositoryDownloadMaster(xmlmodel.Model):
    TAG_NAME = "master"

    url: str = xmlmodel.AttributeField(
        "url",
    )

    sslfingerprint: Optional[str] = xmlmodel.AttributeField(
        "sslfingerprint",
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
