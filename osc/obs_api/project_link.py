from . import xmlmodel


class ProjectLink(xmlmodel.Model):
    TAG_NAME = "link"

    project = xmlmodel.AttributeField(
        "project",
    )

    vrevmode = xmlmodel.AttributeField(
        "vrevmode",
        choices=('unextend', 'extend'),
        optional=True,
    )
