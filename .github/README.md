[![unit tests](https://github.com/openSUSE/osc/actions/workflows/tests.yaml/badge.svg)](https://github.com/openSUSE/osc/actions/workflows/tests.yaml)
[![docs](https://readthedocs.org/projects/opensuse-commander/badge/?version=latest)](https://opensuse-commander.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/openSUSE/osc/branch/master/graph/badge.svg)](https://codecov.io/gh/openSUSE/osc)
[![code climate](https://github.com/openSUSE/osc/actions/workflows/codeql.yml/badge.svg)](https://github.com/openSUSE/osc/actions/workflows/codeql.yml)
[![contributors](https://img.shields.io/github/contributors/openSUSE/osc.svg)](https://github.com/openSUSE/osc/graphs/contributors)


# openSUSE Commander

OpenSUSE Commander (osc) is a command-line interface to the
[Open Build Service (OBS)](https://github.com/openSUSE/open-build-service/).


## Roadmap

* Changes in packaging

[ ] Build osc for all %pythons
[ ] Support Python virtual envs
[ ] Split osc into several subpackages

* Config parser

 [ ] We don’t want to maintain yet another config parser
 [ ] Replace with an INI parser library?
 [ ] Migrate to TOML?
 [ ] Something that preserves comments

* Working with XML
  [ ] XML should not be part of osc public API
  [ ] Osc contributors shouldn’t touch XML unless they really have to
  [ ] How about to generate classes wrapping XML from OBS RelaxNG schemas?

* Working with XPath
  [ ] Building XPath queries is prone to errors
  [ ] Wouldn’t generating XPaths from function arguments be more readable?

* Argcomplete
  [ ] The current completion is hand-crafted
  [ ] We’d like to use argcomplete instead
      * Requires argument sanitization
      * “project package” vs “project/package”
