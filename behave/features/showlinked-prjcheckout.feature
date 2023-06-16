Feature: `osc showlinked` command


# common steps for all scenarios
Background:
   Given I set working directory to "{context.osc.temp}"
     And I execute osc with args "checkout test:factory"
     And I set working directory to "{context.osc.temp}/test:factory"


Scenario: Run `osc showlinked`
    When I execute osc with args "showlinked"
    Then the exit code is 1
     And stderr is
        """
        Directory '{context.osc.temp}/test:factory' is not a working copy of a package
        """