from . import xmlmodel


class RepositoryMaster(xmlmodel.Model):
    TAG_NAME = "master"

    url = xmlmodel.AttributeField(
        "url",
    )

    sslfingerprint = xmlmodel.AttributeField(
        "sslfingerprint",
        optional=True,
    )
