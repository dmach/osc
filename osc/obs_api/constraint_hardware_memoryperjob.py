# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from . import xmlmodel
from .size_unit import SizeUnit


class ConstraintHardwareMemoryperjob(xmlmodel.Model):
    TAG_NAME = "memoryperjob"

    size: SizeUnit = xmlmodel.ModelField(
        "size",
        model_class=SizeUnit,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
