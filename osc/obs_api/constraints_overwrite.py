# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from . import xmlmodel
from .constraints_overwrite_conditions import ConstraintsOverwriteConditions


class ConstraintsOverwrite(xmlmodel.Model):
    TAG_NAME = "overwrite"

    conditions: ConstraintsOverwriteConditions = xmlmodel.ModelField(
        "conditions",
        model_class=ConstraintsOverwriteConditions,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
