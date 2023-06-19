from . import xmlmodel
from .project_maintains import ProjectMaintains


class ProjectMaintenance(xmlmodel.Model):
    TAG_NAME = "maintenance"

    maintainss = xmlmodel.ModelListField(
        "maintains",
        model_class=ProjectMaintains,
    )
