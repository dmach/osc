# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional
from typing import Tuple

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

    name: str = xmlmodel.AttributeField(
        "name",
    )

    kind: Optional[str] = xmlmodel.AttributeField(
        "kind",
        choices=('standard', 'maintenance', 'maintenance_incident', 'maintenance_release'),
        optional=True,
    )

    title: str = xmlmodel.TextNodeField(
        "title",
    )

    description: str = xmlmodel.TextNodeField(
        "description",
    )

    url: Optional[str] = xmlmodel.TextNodeField(
        "url",
        optional=True,
    )

    links: Optional[Tuple[ProjectLink]] = xmlmodel.ModelListField(
        "link",
        model_class=ProjectLink,
        optional=True,
    )

    mountproject: Optional[str] = xmlmodel.TextNodeField(
        "mountproject",
        optional=True,
    )

    remoteurl: Optional[str] = xmlmodel.TextNodeField(
        "remoteurl",
        optional=True,
    )

    scmsync: Optional[str] = xmlmodel.TextNodeField(
        "scmsync",
        optional=True,
    )

    devel: Optional[ProjectDevel] = xmlmodel.ModelField(
        "devel",
        model_class=ProjectDevel,
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

    access: Optional[str] = xmlmodel.EnableDisableField(
        "access",
        optional=True,
    )

    maintenance: Optional[ProjectMaintenance] = xmlmodel.ModelField(
        "maintenance",
        model_class=ProjectMaintenance,
        optional=True,
    )

    repositories: Optional[Tuple[Repository]] = xmlmodel.ModelListField(
        "repository",
        model_class=Repository,
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.

    @classmethod
    def from_api(cls, apiurl, name):
        from .._private import api
        url_path = ["source", name, "_meta"]
        root = api.get(apiurl, url_path)
        obj = cls(_root=root)
        obj._apiurl = apiurl
        return obj

    def api_create_or_update(self, apiurl=None):
        from .._private import api
        apiurl = apiurl or self._apiurl
        url_path = ["source", self.name, "_meta"]
        xml_response = api.put(apiurl, url_path, data=self.to_bytes())
        # TODO: wrap xml response
