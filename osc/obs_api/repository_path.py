# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from . import xmlmodel


class RepositoryPath(xmlmodel.Model):
    TAG_NAME = "path"

    repository: str = xmlmodel.AttributeField(
        "repository",
    )

    project: str = xmlmodel.AttributeField(
        "project",
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
