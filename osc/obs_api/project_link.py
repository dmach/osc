# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional

from . import xmlmodel


class ProjectLink(xmlmodel.Model):
    TAG_NAME = "link"

    project: str = xmlmodel.AttributeField(
        "project",
    )

    vrevmode: Optional[str] = xmlmodel.AttributeField(
        "vrevmode",
        choices=('unextend', 'extend'),
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
