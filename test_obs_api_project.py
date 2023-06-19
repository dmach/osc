#!/usr/bin/python3


import unittest

from osc.obs_api.project import Project
from osc.obs_api.repository_path import RepositoryPath
from osc.obs_api.flag import Flag

import osc.conf
osc.conf.get_config(override_http_debug=0)


class ProjectTest(unittest.TestCase):
    def test_name(self):
        data = """
<project name="test-name" />
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.name, "test-name")
        self.assertEqual(project.to_string(), data)

        project.name = "CHANGED"
        self.assertEqual(project.name, "CHANGED")
        expected = """<project name="CHANGED" />"""
        self.assertEqual(project.to_string(), expected)

    def test_description(self):
        # create
        data = """
<project name="test-name">
</project>""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.description, None)
        project.description = ""
        expected = """
<project name="test-name">
  <description />
</project>""".strip()
        self.assertEqual(project.to_string(), expected)

        # read
        data = """
<project name="test-name">
  <description>test-desc</description>
</project>""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.description, "test-desc")
        self.assertEqual(project.to_string(), data)

        # update
        project.description = "CHANGED"
        self.assertEqual(project.description, "CHANGED")
        expected = """
<project name="test-name">
  <description>CHANGED</description>
</project>""".strip()
        self.assertEqual(project.to_string(), expected)

        # delete
        self.assertRaises(ValueError, delattr, project, "description")

        # clear
        project.description = ""
        self.assertEqual(project.description, "")
        expected = """
<project name="test-name">
  <description />
</project>""".strip()
        self.assertEqual(project.to_string(), expected)

    def test_kind(self):
        # create
        data = """
<project name="test-name" />
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.kind, None)
        project.kind = "standard"
        expected = """
<project name="test-name" kind="standard" />
""".strip()
        self.assertEqual(project.to_string(), expected)

        # read
        data = """
<project name="test-name" kind="standard" />
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.kind, "standard")
        self.assertEqual(project.to_string(), data)

        # update
        #self.assertRaises(ValueError, setattr, project, "kind", "CHANGED")
        project.kind = "maintenance"
        self.assertEqual(project.kind, "maintenance")
        expected = """
<project name="test-name" kind="maintenance" />
""".strip()
        self.assertEqual(project.to_string(), expected)

        # delete
        del project.kind
        expected = """
<project name="test-name" />
""".strip()
        self.assertEqual(project.to_string(), expected)

    def test_lock(self):
        # create
        data = """
<project name="test-name" />
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.lock, None)
        project.lock = "enable"
        expected = """
<project name="test-name">
  <lock>
    <enable />
  </lock>
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

        # read
        data = """
<project name="test-name">
  <lock>
    <disable />
  </lock>
</project>
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.lock, "disable")
        self.assertEqual(project.to_string(), data)

        # update
        self.assertRaises(ValueError, setattr, project, "lock", "CHANGED")
        project.lock = "enable"
        self.assertEqual(project.lock, "enable")
        expected = """
<project name="test-name">
  <lock>
    <enable />
  </lock>
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

        # delete
        del project.lock
        expected = """
<project name="test-name" />
""".strip()
        self.assertEqual(project.to_string(), expected)

    def test_repository(self):
        data = """
<project name="test-name">
  <repository name="snapshot">
    <path project="openSUSE:Tumbleweed" repository="standard"/>
    <arch>x86_64</arch>
    <arch>i586</arch>
  </repository>
</project>
""".strip()
        project = Project.from_string(data)
        self.assertEqual(len(project.repositories), 1)

        repo = project.repositories[0]
        self.assertEqual(repo.name, "snapshot")
        self.assertEqual(repo.archs, ("x86_64", "i586"))

        self.assertEqual(len(repo.paths), 1)
        path = repo.paths[0]
        self.assertEqual(path.project, "openSUSE:Tumbleweed")
        self.assertEqual(path.repository, "standard")

        repo.paths = (
            RepositoryPath.new(project="foo", repository="bar"),
        )

        self.assertEqual(len(repo.paths), 1)
        path = repo.paths[0]
        self.assertEqual(path.project, "foo")
        self.assertEqual(path.repository, "bar")
        project.to_string()

    def test_build(self):
        data = """
<project name="test-name">
  <build>
    <enable arch="i586" repository="qwerty"/>
  </build>
</project>
""".strip()
        project = Project.from_string(data)
        self.assertNotEqual(project.build, ())

        x = project.build[0]
        print(x.flag, x.arch, x.repository)

        print(project.to_string())

        project.build += (Flag.new("enable"), )
        project.build += (Flag.new("disable", arch="x86_64"), )
        project.build += (Flag.new("disable", arch="x86_64", repository="asdasd"), )
        print(project.to_string())


if __name__ == "__main__":
    unittest.main()
