#!/usr/bin/python3

import importlib
import os
import pkgutil
import sys
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import osc
import osc._private

#for loader, module_name, _ in pkgutil.iter_modules(path=["generated-classes"], prefix=""):
#    print(loader, module_name, _)
#loader = importlib.find_loader("osc._private.objects", path="generated-classes")
spec = importlib.util.spec_from_file_location("osc._private.objects", os.path.abspath("generated_classes/__init__.py"))
mod = importlib.util.module_from_spec(spec)
sys.modules["osc._private.objects"] = mod
spec.loader.exec_module(mod)


from osc._private.objects import *

import osc.conf
osc.conf.get_config(override_http_debug=0)


# TODO: no criteria -> error
# TODO: __repr__() for all generated classes (that have name?)


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
        self.assertRaises(ValueError, setattr, project, "kind", "CHANGED")
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
        self.assertEqual(repo.paths, ({"project": "openSUSE:Tumbleweed", "repository": "standard"}, ))
        repo.paths = (
            {"project": "foo", "repository": "bar"},
        )
        self.assertEqual(repo.paths, ({"project": "foo", "repository": "bar"}, ))
#        repo.paths = (
#            {"invalid": "foo"},
#        )
        # TODO: invalid key(s)
        # TODO: incomplete key(s)

    def test_build(self):
        data = """
<project name="test-name" />
""".strip()
        project = Project.from_string(data)
        self.assertEqual(project.build, None)
        project.build = (
            {"flag": "disable", "repository": "standard", "arch": "x86_64"},
        )
        # TODO: add (iadd aka +=)? remove?
#        project.build = [...]
#        self.assertEqual(project.to_string(), data)


if __name__ == "__main__":
    unittest.main()


apiurl = "https://localhost:1443"
projects = Project.search(apiurl, name__contains=":factory")
#print(x)
for p in projects:
    print()
    print(p.name)
#    print(f"build: >{p.build}<")
    '''
    p.lock = "enable"
    print(f"lock: >{p.lock}<")
    p.lock = "disable"
    print(f"lock: >{p.lock}<")

    print(p.repositories)
    for r in p.repositories:
        print("N", r.name)
        print("P", r.paths)
        print("A", r.archs)
#        print(r.foo)

#    p.repositories = [{'repository': 'openSUSE_Tumbleweed', 'project': 'home:darix:container-workshop'}, {'repository': 'containers', 'project': 'openSUSE:Templates:Images:Tumbleweed'}]
    print(p.repositories)
    '''

    print(p.build)
    print(len(p.build))
    for i in p.build:
        print(i.state, i.arch, i.repository)


print(p.to_string())

1/0
apiurl = "https://api.opensuse.org"
x = Project.search(apiurl, name__contains="darix:")
#print(x)
for i in x:
    print()
    print(i.name)
    print(i.title)
    print(i.kind)
    print(i.description)
    print(i.repositories)
    for r in i.repositories:
        print(r.name)
        print(r.paths)
        print(r.archs)



#from objects.