# This is an osc plugin, place it under ~/.local/lib/osc-plugins or /usr/lib/osc-plugins


import difflib

from osc import cmdln
from osc import oscerr
from osc._private import api
from osc.core import ET
from osc.core import raw_input


# TODO: move to osc._private.api
# TODO: add file=...
def put(apiurl, path, query=None, data=None):
    """
    Send a PUT request to OBS.

    :param apiurl: OBS apiurl.
    :type  apiurl: str
    :param path: URL path segments.
    :type  path: list(str)
    :param query: URL query values.
    :type  query: dict(str, str)
    :returns: Parsed XML root.
    :rtype:   xml.etree.ElementTree.Element
    """
    from osc import connection as osc_connection
    from osc import core as osc_core

    assert apiurl
    assert path

    if not isinstance(path, (list, tuple)):
        raise TypeError("Argument `path` expects a list of strings")

    url = osc_core.makeurl(apiurl, path, query)
    with osc_connection.http_PUT(url, data=data) as f:
        root = osc_core.ET.parse(f).getroot()
    return root


def group_child_nodes(node):
    nodes = node[:]
    result = []

    while nodes:
        # look at the tag of the first node
        tag = nodes[0].tag

        # collect all nodes with the same tag and append them to the result
        # process nodes with the different tags in the following iterations
        matches = []
        others = []
        for i in nodes:
            if i.tag == tag:
                matches.append(i)
            else:
                others.append(i)

        result += matches
        nodes = others

    node[:] = result


class APIXMLBase:
    def __init__(self, xml_root):
        self.root = xml_root

    def to_bytes(self):
        ET.indent(self.root, space="  ", level=0)
        return ET.tostring(self.root, encoding="utf-8")

    def to_string(self):
        return self.to_bytes().decode("utf-8")


class ProjectMeta(APIXMLBase):
    @classmethod
    def from_api(cls, apiurl, project):
        url_path = ["source", project, "_meta"]
        root = api.get(apiurl, url_path)
        obj = cls(root)
        return obj

    def __init__(self, xml_root):
        self.root = xml_root

    def to_api(self, apiurl, project):
        url_path = ["source", project, "_meta"]
        put(apiurl, url_path, data=self.to_bytes())

    def disable_repo(self, name: str):
        node = api.find_node(self.root, "project", "publish")
        if node is None:
            project_node = api.find_node(self.root, "project")
            node = ET.SubElement(project_node, "publish")
        else:
            existing = api.find_node(node, "publish", "disable", {"repository": name})
            if existing is not None:
                return

        ET.SubElement(node, "disable", attrib={"repository": name})
        group_child_nodes(node)

    def add_repository(self, name, arches, paths):
        node = api.find_node(self.root, "project")

        existing = api.find_node(self.root, "project", "repository", {"name": name})
        if existing:
            raise oscerr.OscValueError(f"Repository '{name}' already exists in project meta")

        repo_node = ET.SubElement(node, "repository", attrib={"name": name})

        for path_data in paths:
            ET.SubElement(repo_node, "path", attrib={
                "project": path_data["project"],
                "repository": path_data["repository"],
            })

        for arch in arches:
            arch_node = ET.SubElement(repo_node, "arch")
            arch_node.text = arch

        group_child_nodes(repo_node)
        group_child_nodes(node)


@cmdln.option("project")
@cmdln.option("--repo", required=True)
@cmdln.option("--arch", dest="arches", metavar="[ARCH]", action="append", required=True)
@cmdln.option("--path", dest="paths", metavar="[PROJECT/REPO]", action="append", required=True)
@cmdln.option("--disabled", action="store_true", default=False, help="Disable the added repository")
@cmdln.option("--yes", action="store_true", help="Proceed without asking")
@cmdln.name("repo-add")
def do_repo_add(self, subcmd, opts):
    """
    Add new repository to projet meta.
    """
    apiurl = self.get_api_url()

    paths = []
    for path in opts.paths:
        if "/" not in path:
            self.argparse_error(f"Invalid path (expected format is PROJECT/REPO): {path}")
        project, repo = path.split("/")
        paths.append({"project": project, "repository": repo})

    meta = ProjectMeta.from_api(apiurl, opts.project)
    old_meta = meta.to_string().splitlines()

    meta.add_repository(opts.repo, opts.arches, paths)
    if opts.disabled:
        meta.disable_repo(opts.repo)

    new_meta = meta.to_string().splitlines()
    diff = difflib.unified_diff(old_meta, new_meta, fromfile="old", tofile="new")
    print("\n".join(diff))

    if not opts.yes:
        print()
        print(f"You're changing meta of project '{opts.project}'")
        reply = raw_input("Do you want to apply the changes? [y/N] ").lower()
        if reply != "y":
            raise oscerr.UserAbort()

    meta.to_api(apiurl, opts.project)
