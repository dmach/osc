# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Tuple

from . import xmlmodel
from .project_maintenance_maintains import ProjectMaintenanceMaintains


class ProjectMaintenance(xmlmodel.Model):
    TAG_NAME = "maintenance"

    maintains: Tuple[ProjectMaintenanceMaintains] = xmlmodel.ModelListField(
        "maintains",
        model_class=ProjectMaintenanceMaintains,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
