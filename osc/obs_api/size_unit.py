# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from . import xmlmodel


class SizeUnit(xmlmodel.Model):
    TAG_NAME = "size"

    unit: str = xmlmodel.AttributeField(
        "unit",
        choices=('K', 'M', 'G', 'T'),
    )

    data: str = xmlmodel.DataField(
        "data",
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
