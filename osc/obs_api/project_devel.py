from . import xmlmodel


class ProjectDevel(xmlmodel.Model):
    TAG_NAME = "devel"

    project = xmlmodel.AttributeField(
        "project",
    )
