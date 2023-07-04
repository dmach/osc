#!/usr/bin/python3


import unittest

from osc.obs_api.constraints import Constraints
#from osc.obs_api.repository_path import RepositoryPath
#from osc.obs_api.flag import Flag

#from osc.obs_api.xmlmodel import InvalidChoice
#from osc.obs_api.xmlmodel import ValueRequiredError


class ConstraintsTest(unittest.TestCase):

    def test_create(self):
        c = Constraints()
        c.hardware = {
            "cpu": {
                "flags": [
                    {"data": "aarch64"},
                    {"exclude": "true", "data": "x86_64"},
                ],
            },
            "physicalmemory": {
                "size": {
                    "unit": "G",
                    "data": "10",
                },
            },
        }
        c.hardware.memory = {
            "size": {
                "unit": "G",
                "data": "1.5",
            },
        }
        expected = """
<constraints>
  <hardware>
    <cpu>
      <flag>aarch64</flag>
      <flag exclude="true">x86_64</flag>
    </cpu>
    <memory>
      <size unit="G">1.5</size>
    </memory>
    <physicalmemory>
      <size unit="G">10</size>
    </physicalmemory>
  </hardware>
</constraints>
""".strip()
        self.assertEqual(c.to_string(), expected)
        print(dir(type(c.hardware)))
#        c.hardware.memory = {"size": [{}]}
        #{"size": {"unit": "G", "data": "1.5"}}

#    <memory>
#      <size unit="G">1.5</size>
#    </memory>
#    <physicalmemory>
#      <size unit="M">512</size>
#    </physicalmemory>

        print(c.to_string())


if __name__ == "__main__":
    unittest.main()
