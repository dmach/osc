# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional

from . import xmlmodel


class ConstraintHostlabel(xmlmodel.Model):
    TAG_NAME = "hostlabel"

    exclude: Optional[str] = xmlmodel.AttributeField(
        "exclude",
        choices=('false', 'true'),
        optional=True,
    )

    data: str = xmlmodel.DataField(
        "data",
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
