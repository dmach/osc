# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from . import xmlmodel
from . import choices


class Person(xmlmodel.Model):
    TAG_NAME = "person"

    userid: str = xmlmodel.AttributeField(
        "userid",
    )

    role: str = xmlmodel.AttributeField(
        "role",
        choices=choices.LOCAL_ROLE,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
