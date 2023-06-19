from . import xmlmodel


class RepositoryHostsystem(xmlmodel.Model):
    TAG_NAME = "hostsystem"

    repository = xmlmodel.AttributeField(
        "repository",
    )

    project = xmlmodel.AttributeField(
        "project",
    )
