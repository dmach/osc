from . import xmlmodel
from . import choices


class Group(xmlmodel.Model):
    TAG_NAME = "group"

    groupid = xmlmodel.AttributeField(
        "groupid",
    )

    role = xmlmodel.AttributeField(
        "role",
        choices=choices.LOCAL_ROLE,
    )
