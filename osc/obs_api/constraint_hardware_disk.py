# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from . import xmlmodel
from .size_unit import SizeUnit


class ConstraintHardwareDisk(xmlmodel.Model):
    TAG_NAME = "disk"

    size: SizeUnit = xmlmodel.ModelField(
        "size",
        model_class=SizeUnit,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
