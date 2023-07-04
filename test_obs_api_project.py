#!/usr/bin/python3


import unittest

from osc.obs_api.project import Project
from osc.obs_api.repository_path import RepositoryPath
from osc.obs_api.flag import Flag

from osc.obs_api.xmlmodel import InvalidChoice
from osc.obs_api.xmlmodel import ValueRequiredError


class ProjectTest(unittest.TestCase):

    def test_name(self):
        data = """
<project name="project-name">
  <title />
  <description />
</project>
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.to_string(), data)
        self.assertEqual(project.name, "project-name")

        project.name = "new-name"
        self.assertEqual(project.name, "new-name")

        expected = """
<project name="new-name">
  <title />
  <description />
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

        self.assertRaises(ValueRequiredError, delattr, project, "name")
        self.assertRaises(ValueRequiredError, setattr, project, "name", None)

    def test_title(self):
        data = """
<project name="project-name">
  <title />
  <description />
</project>
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.to_string(), data)
        self.assertEqual(project.title, "")

        project.title = "new-title"
        self.assertEqual(project.title, "new-title")

        expected = """
<project name="project-name">
  <title>new-title</title>
  <description />
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

        self.assertRaises(ValueRequiredError, delattr, project, "title")
        self.assertRaises(ValueRequiredError, setattr, project, "title", None)

    def test_description(self):
        data = """
<project name="project-name">
  <title />
  <description />
</project>
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.to_string(), data)
        self.assertEqual(project.description, "")

        project.description = "new-description"
        self.assertEqual(project.description, "new-description")

        expected = """
<project name="project-name">
  <title />
  <description>new-description</description>
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

        self.assertRaises(ValueRequiredError, delattr, project, "description")
        self.assertRaises(ValueRequiredError, setattr, project, "description", None)

    def test_kind(self):
        data = """
<project name="project-name">
  <title />
  <description />
</project>
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.to_string(), data)
        self.assertEqual(project.kind, None)

        project.kind = "standard"
        expected = """
<project name="project-name" kind="standard">
  <title />
  <description />
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

        self.assertRaises(InvalidChoice, setattr, project, "kind", "INVALID")

        del project.kind
        expected = """
<project name="project-name">
  <title />
  <description />
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

    def test_lock(self):
        data = """
<project name="project-name">
  <title />
  <description />
</project>
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.lock, None)

        project.lock = "enable"
        expected = """
<project name="project-name">
  <title />
  <description />
  <lock>
    <enable />
  </lock>
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

        self.assertRaises(InvalidChoice, setattr, project, "lock", "INVALID")
        project.lock = "disable"
        self.assertEqual(project.lock, "disable")
        expected = """
<project name="project-name">
  <title />
  <description />
  <lock>
    <disable />
  </lock>
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

        # delete
        del project.lock
        expected = """
<project name="project-name">
  <title />
  <description />
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

    def test_repository(self):
        data = """
<project name="project-name">
  <title />
  <description />
</project>
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.repositories, ())
#        self

        project.repositories = (
            {
                "name": "snapshot",
                "archs": ("x86_64", "i586"),
                "paths": (),
            },
        )

        expected = """
<project name="project-name">
  <title />
  <description />
  <repository name="snapshot">
    <arch>x86_64</arch>
    <arch>i586</arch>
  </repository>
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

        project.repositories = None
        expected = """
<project name="project-name">
  <title />
  <description />
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

    def test_build(self):
        data = """
<project name="project-name">
  <title />
  <description />
</project>
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.build, ())

        project.build += (
            {"flag": "enable"},
            {"flag": "disable", "arch": "x86_64"},
            {"flag": "disable", "arch": "x86_64", "repository": "foobar"},
        )
        self.assertEqual(len(project.build), 3)

        self.assertEqual(project.build[0].flag, "enable")
        self.assertEqual(project.build[0].arch, None)
        self.assertEqual(project.build[0].repository, None)

        self.assertEqual(project.build[1].flag, "disable")
        self.assertEqual(project.build[1].arch, "x86_64")
        self.assertEqual(project.build[1].repository, None)

        self.assertEqual(project.build[2].flag, "disable")
        self.assertEqual(project.build[2].arch, "x86_64")
        self.assertEqual(project.build[2].repository, "foobar")

        expected = """
<project name="project-name">
  <title />
  <description />
  <build>
    <enable />
    <disable arch="x86_64" />
    <disable arch="x86_64" repository="foobar" />
  </build>
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)

    def test_maintenance(self):
        data = """
<project name="project-name">
  <title />
  <description />
</project>
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.build, ())

        project.maintenance = {
            "maintains": (
                {"project": "foo"},
                {"project": "bar"},
            )
        }

        expected = """
<project name="project-name">
  <title />
  <description />
  <maintenance>
    <maintains project="foo" />
    <maintains project="bar" />
  </maintenance>
</project>
""".strip()
        self.assertEqual(project.to_string(), expected)


if __name__ == "__main__":
    unittest.main()
