from . import xmlmodel
from .flag import Flag
from .group import Group
from .person import Person
from .project_devel import ProjectDevel
from .project_link import ProjectLink
from .project_maintenance import ProjectMaintenance
from .repository import Repository


class Project(xmlmodel.Model):
    TAG_NAME = "project"

    name = xmlmodel.AttributeField(
        "name",
        optional=True,
    )

    kind = xmlmodel.AttributeField(
        "kind",
        choices=('standard', 'maintenance', 'maintenance_incident', 'maintenance_release'),
        optional=True,
    )

    title = xmlmodel.TextNodeField(
        "title",
    )

    description = xmlmodel.TextNodeField(
        "description",
    )

    url = xmlmodel.TextNodeField(
        "url",
        optional=True,
    )

    links = xmlmodel.ModelListField(
        "link",
        model_class=ProjectLink,
        optional=True,
    )

    mountproject = xmlmodel.TextNodeField(
        "mountproject",
        optional=True,
    )

    remoteurl = xmlmodel.TextNodeField(
        "remoteurl",
        optional=True,
    )

    scmsync = xmlmodel.TextNodeField(
        "scmsync",
        optional=True,
    )

    devel = xmlmodel.ModelField(
        "devel",
        model_class=ProjectDevel,
        optional=True,
    )

    persons = xmlmodel.ModelListField(
        "person",
        model_class=Person,
        optional=True,
    )

    groups = xmlmodel.ModelListField(
        "group",
        model_class=Group,
        optional=True,
    )

    lock = xmlmodel.EnableDisableField(
        "lock",
        optional=True,
    )

    lock = xmlmodel.TextNodeField(
        "lock",
        optional=True,
    )

    build = xmlmodel.ModelListField(
        name="build",
        model_class=Flag,
        optional=True,
        outer_tag_name="build",
    )

    publish = xmlmodel.ModelField(
        "publish",
        model_class=Flag,
        optional=True,
    )

    useforbuild = xmlmodel.ModelField(
        "useforbuild",
        model_class=Flag,
        optional=True,
    )

    debuginfo = xmlmodel.ModelField(
        "debuginfo",
        model_class=Flag,
        optional=True,
    )

    binarydownload = xmlmodel.ModelField(
        "binarydownload",
        model_class=Flag,
        optional=True,
    )

    sourceaccess = xmlmodel.EnableDisableField(
        "sourceaccess",
        optional=True,
    )

    sourceaccess = xmlmodel.TextNodeField(
        "sourceaccess",
        optional=True,
    )

    access = xmlmodel.EnableDisableField(
        "access",
        optional=True,
    )

    access = xmlmodel.TextNodeField(
        "access",
        optional=True,
    )

    maintenance = xmlmodel.ModelField(
        "maintenance",
        model_class=ProjectMaintenance,
        optional=True,
    )

    repositories = xmlmodel.ModelListField(
        "repository",
        model_class=Repository,
        optional=True,
    )
