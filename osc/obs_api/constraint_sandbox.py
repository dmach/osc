# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional

from . import xmlmodel


class ConstraintSandbox(xmlmodel.Model):
    TAG_NAME = "sandbox"

    exclude: Optional[str] = xmlmodel.AttributeField(
        "exclude",
        choices=('false', 'true'),
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
