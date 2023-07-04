from . import choices
from . import xmlmodel


class Flag(xmlmodel.Model):
    TAG_NAME = ("disable", "enable")

    def __init__(self, **kwargs):
        if "_root" not in kwargs:
            flag = kwargs.get("flag")
            kwargs["_root"] = xmlmodel.xml.ET.Element(flag)
        super().__init__(**kwargs)

    flag = xmlmodel.TagNameField(
        choices=TAG_NAME,
        # TODO:
        help_text=None,
    )

    repository = xmlmodel.AttributeField(
        "repository",
        optional=True,
        # TODO:
        help_text=None,
    )

    arch = xmlmodel.AttributeField(
        "arch",
        choices=choices.BUILD_ARCH,
        optional=True,
        # TODO:
        help_text=None,
    )
