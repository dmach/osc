# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Tuple

from . import xmlmodel
from .constraint_hardware_cpu_flag import ConstraintHardwareCpuFlag


class ConstraintHardwareCpu(xmlmodel.Model):
    TAG_NAME = "cpu"

    flags: Tuple[ConstraintHardwareCpuFlag] = xmlmodel.ModelListField(
        "flag",
        model_class=ConstraintHardwareCpuFlag,
        help_text=(
            "All cpu flags from /proc/cpuinfo can required here. In addition also pseudo helper",
            "flags for an architecture level: power7, power8, power9, EL0, x86-64-v2, x86-64-v3, x86-64-v4",
        ),
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
