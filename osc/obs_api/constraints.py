# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional
from typing import Tuple

from . import xmlmodel
from .constraint_hardware import ConstraintHardware
from .constraint_hostlabel import ConstraintHostlabel
from .constraint_linux import ConstraintLinux
from .constraint_sandbox import ConstraintSandbox
from .constraints_overwrite import ConstraintsOverwrite


class Constraints(xmlmodel.Model):
    TAG_NAME = "constraints"

    overwrites: Optional[Tuple[ConstraintsOverwrite]] = xmlmodel.ModelListField(
        "overwrite",
        model_class=ConstraintsOverwrite,
        optional=True,
    )

    hostlabels: Optional[Tuple[ConstraintHostlabel]] = xmlmodel.ModelListField(
        "hostlabel",
        model_class=ConstraintHostlabel,
        optional=True,
    )

    sandboxes: Optional[Tuple[ConstraintSandbox]] = xmlmodel.ModelListField(
        "sandbox",
        model_class=ConstraintSandbox,
        optional=True,
    )

    linux: Optional[ConstraintLinux] = xmlmodel.ModelField(
        "linux",
        model_class=ConstraintLinux,
        optional=True,
    )

    hardware: Optional[ConstraintHardware] = xmlmodel.ModelField(
        "hardware",
        model_class=ConstraintHardware,
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
