from . import xmlmodel
from . import choices


class Person(xmlmodel.Model):
    TAG_NAME = "person"

    userid = xmlmodel.AttributeField(
        "userid",
    )

    role = xmlmodel.AttributeField(
        "role",
        choices=choices.LOCAL_ROLE,
    )
