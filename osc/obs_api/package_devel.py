# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional

from . import xmlmodel


class PackageDevel(xmlmodel.Model):
    TAG_NAME = "devel"

    project: Optional[str] = xmlmodel.AttributeField(
        "project",
        optional=True,
    )

    package: Optional[str] = xmlmodel.AttributeField(
        "package",
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
