from . import xmlmodel


class RepositoryPath(xmlmodel.Model):
    TAG_NAME = "path"

    repository = xmlmodel.AttributeField(
        "repository",
    )

    project = xmlmodel.AttributeField(
        "project",
    )
