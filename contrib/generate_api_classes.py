#!/usr/bin/python3


import os
import sys
from xml.etree import ElementTree as ET

DIR = os.path.abspath(os.path.dirname(__file__))
OBS_DIR = os.path.join(DIR, "open-build-service")


if not os.path.exists(OBS_DIR):
    print(f"ERROR: The Open Build Service checkout doesn't exist: {OBS_DIR}", file=sys.stderr)
    print("Run the following commands first:", file=sys.stderr)
    print(f"  cd {DIR}", file=sys.stderr)
    print("  git clone https://github.com/openSUSE/open-build-service.git", file=sys.stderr)
    sys.exit(1)


class SchemaParser:
    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.root = None

    def to_string(self):
        ET.indent(self.root)
        return ET.tostring(self.root, encoding="utf-8").decode("utf-8")

    @staticmethod
    def ln(node):
        """
        Return local name (name without a namespace) of the ``node``.
        """
        return node.tag.split("}")[-1]

    def _parse(self, path):
        """
        Parse XML in given ``path``, return the root element.
        """
        doc = ET.parse(path)
        root = doc.getroot()
        return root

    def _expand_includes(self, node):
        """
        Replace includes with the content of the referenced schemas.
        """
        if self.ln(node) == "include":
            href = node.get("href")
            path = os.path.join(os.path.dirname(self.path), href)
            root = self._parse(path)
            self._expand_includes(root)
            return root[:]

        new_nodes = []
        for child in node:
            nodes = self._expand_includes(child)
            if nodes is None:
                continue
            if not isinstance(nodes, list):
                nodes = [nodes]
            new_nodes.extend(nodes)
        node[:] = new_nodes

        return node

    def parse(self):
        self.root = self._parse(self.path)
        assert self.ln(self.root) == "grammar"

        self._expand_includes(self.root)

        result = {}
        return result


def main():
    path = os.path.join(OBS_DIR, "docs/api/api/project.rng")
    parser = SchemaParser(path)
    parsed_schema = parser.parse()
    # print(parser.to_string())


if __name__ == "__main__":
    main()
