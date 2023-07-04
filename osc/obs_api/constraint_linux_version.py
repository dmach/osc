# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional

from . import xmlmodel


class ConstraintLinuxVersion(xmlmodel.Model):
    TAG_NAME = "version"

    max: Optional[str] = xmlmodel.TextNodeField(
        "max",
        optional=True,
    )

    min: Optional[str] = xmlmodel.TextNodeField(
        "min",
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
