# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional

from . import xmlmodel
from .constraint_hardware_cpu import ConstraintHardwareCpu
from .constraint_hardware_disk import ConstraintHardwareDisk
from .constraint_hardware_memory import ConstraintHardwareMemory
from .constraint_hardware_memoryperjob import ConstraintHardwareMemoryperjob
from .constraint_hardware_physicalmemory import ConstraintHardwarePhysicalmemory


class ConstraintHardware(xmlmodel.Model):
    TAG_NAME = "hardware"

    cpu: Optional[ConstraintHardwareCpu] = xmlmodel.ModelField(
        "cpu",
        model_class=ConstraintHardwareCpu,
        optional=True,
    )

    processors: Optional[str] = xmlmodel.TextNodeField(
        "processors",
        optional=True,
    )

    jobs: Optional[str] = xmlmodel.TextNodeField(
        "jobs",
        optional=True,
    )

    disk: Optional[ConstraintHardwareDisk] = xmlmodel.ModelField(
        "disk",
        model_class=ConstraintHardwareDisk,
        optional=True,
    )

    memory: Optional[ConstraintHardwareMemory] = xmlmodel.ModelField(
        "memory",
        model_class=ConstraintHardwareMemory,
        optional=True,
    )

    memoryperjob: Optional[ConstraintHardwareMemoryperjob] = xmlmodel.ModelField(
        "memoryperjob",
        model_class=ConstraintHardwareMemoryperjob,
        optional=True,
    )

    physicalmemory: Optional[ConstraintHardwarePhysicalmemory] = xmlmodel.ModelField(
        "physicalmemory",
        model_class=ConstraintHardwarePhysicalmemory,
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
