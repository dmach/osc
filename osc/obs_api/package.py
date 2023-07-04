# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional
from typing import Tuple

from . import xmlmodel
from .flag import Flag
from .group import Group
from .package_devel import PackageDevel
from .person import Person


class Package(xmlmodel.Model):
    TAG_NAME = "package"

    name: str = xmlmodel.AttributeField(
        "name",
    )

    project: str = xmlmodel.AttributeField(
        "project",
    )

    title: str = xmlmodel.TextNodeField(
        "title",
    )

    description: str = xmlmodel.TextNodeField(
        "description",
    )

    devel: Optional[PackageDevel] = xmlmodel.ModelField(
        "devel",
        model_class=PackageDevel,
        optional=True,
    )

    releasename: Optional[str] = xmlmodel.TextNodeField(
        "releasename",
        optional=True,
    )

    persons: Optional[Tuple[Person]] = xmlmodel.ModelListField(
        "person",
        model_class=Person,
        optional=True,
    )

    groups: Optional[Tuple[Group]] = xmlmodel.ModelListField(
        "group",
        model_class=Group,
        optional=True,
    )

    lock: Optional[str] = xmlmodel.EnableDisableField(
        "lock",
        optional=True,
    )

    build: Optional[Tuple[Flag]] = xmlmodel.ModelListField(
        "build",
        model_class=Flag,
        optional=True,
        has_outer_tag=True,
    )

    publish: Optional[Tuple[Flag]] = xmlmodel.ModelListField(
        "publish",
        model_class=Flag,
        optional=True,
        has_outer_tag=True,
    )

    useforbuild: Optional[Tuple[Flag]] = xmlmodel.ModelListField(
        "useforbuild",
        model_class=Flag,
        optional=True,
        has_outer_tag=True,
    )

    debuginfo: Optional[Tuple[Flag]] = xmlmodel.ModelListField(
        "debuginfo",
        model_class=Flag,
        optional=True,
        has_outer_tag=True,
    )

    binarydownload: Optional[Tuple[Flag]] = xmlmodel.ModelListField(
        "binarydownload",
        model_class=Flag,
        optional=True,
        has_outer_tag=True,
    )

    sourceaccess: Optional[str] = xmlmodel.EnableDisableField(
        "sourceaccess",
        optional=True,
    )

    url: Optional[str] = xmlmodel.TextNodeField(
        "url",
        optional=True,
    )

    scmsync: Optional[str] = xmlmodel.TextNodeField(
        "scmsync",
        optional=True,
    )

    bcntsynctag: Optional[str] = xmlmodel.TextNodeField(
        "bcntsynctag",
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
