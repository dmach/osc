# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional

from . import xmlmodel
from .constraint_linux_version import ConstraintLinuxVersion


class ConstraintLinux(xmlmodel.Model):
    TAG_NAME = "linux"

    version: Optional[ConstraintLinuxVersion] = xmlmodel.ModelField(
        "version",
        model_class=ConstraintLinuxVersion,
        optional=True,
    )

    flavor: Optional[str] = xmlmodel.TextNodeField(
        "flavor",
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
