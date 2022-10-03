@no-snapshot
Feature: `osc list` command


Scenario: Run `osc list` with no arguments to display all projects
   When I execute osc with args "list"
   Then stdout is
        """
        home:Admin
        openSUSE.org
        openSUSE:Factory
        """


Scenario: Run `osc list` on a project to display project packages
   When I execute osc with args "list openSUSE:Factory"
   Then stdout is
        """
        multibuild-pkg
        multibuild-pkg:flavor1
        multibuild-pkg:flavor2
        test-pkgA
        test-pkgB
        """


Scenario: Run `osc list` on a project package to display package files
   When I execute osc with args "list openSUSE:Factory test-pkgA"
   Then stdout is
        """
        test-pkgA.changes
        test-pkgA.spec
        """
