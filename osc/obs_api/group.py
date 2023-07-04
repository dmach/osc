# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from . import xmlmodel
from . import choices


class Group(xmlmodel.Model):
    TAG_NAME = "group"

    groupid: str = xmlmodel.AttributeField(
        "groupid",
    )

    role: str = xmlmodel.AttributeField(
        "role",
        choices=choices.LOCAL_ROLE,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
