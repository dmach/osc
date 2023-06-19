from . import xmlmodel
from . import choices


class RepositoryReleasetarget(xmlmodel.Model):
    TAG_NAME = "releasetarget"

    project = xmlmodel.AttributeField(
        "project",
    )

    repository = xmlmodel.AttributeField(
        "repository",
    )

    trigger = xmlmodel.AttributeField(
        "trigger",
        choices=choices.RELEASE_TRIGGERS,
        optional=True,
    )
