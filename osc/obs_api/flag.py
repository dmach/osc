from . import choices
from . import xmlmodel
from .repository import Repository


class Flag(xmlmodel.Model):
    TAG_NAME = ("disable", "enable")

    @classmethod
    def new(cls, flag, **kwargs):
        root = xmlmodel.xml.ET.Element(flag)
        obj = cls(root)

        # just to run validators on the flag
        kwargs["flag"] = flag

        for key, value in kwargs.items():
            setattr(obj, key, value)
        return obj

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
