from . import xmlmodel


class ProjectMaintains(xmlmodel.Model):
    TAG_NAME = "maintains"

    project = xmlmodel.AttributeField(
        "project",
    )
