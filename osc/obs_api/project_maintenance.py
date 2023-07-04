# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Tuple

from . import xmlmodel
from .project_maintains import ProjectMaintains


class ProjectMaintenance(xmlmodel.Model):
    TAG_NAME = "maintenance"

    maintainss: Tuple[ProjectMaintains] = xmlmodel.ModelListField(
        "maintains",
        model_class=ProjectMaintains,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
