from . import xmlmodel


class SizeUnit(xmlmodel.Model):
    TAG_NAME = "size"

    unit = xmlmodel.AttributeField(
        "unit",
        choices=('K', 'M', 'G', 'T'),
    )
