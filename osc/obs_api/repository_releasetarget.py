# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional

from . import xmlmodel
from . import choices


class RepositoryReleasetarget(xmlmodel.Model):
    TAG_NAME = "releasetarget"

    project: str = xmlmodel.AttributeField(
        "project",
    )

    repository: str = xmlmodel.AttributeField(
        "repository",
    )

    trigger: Optional[str] = xmlmodel.AttributeField(
        "trigger",
        choices=choices.RELEASE_TRIGGERS,
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
