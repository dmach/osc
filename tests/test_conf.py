import importlib
import os
import unittest

import osc.conf


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "conf_fixtures")


class TestConf(unittest.TestCase):
    def setUp(self):
        # reset the global `config` in preparation for running the tests
        importlib.reload(osc.conf)

    def tearDown(self):
        # reset the global `config` to avoid impacting tests from other classes
        importlib.reload(osc.conf)

    def _get_fixtures_dir(self):
        return FIXTURES_DIR

    def test_bool_opts_defaults(self):
        config = osc.conf.config
        for opt in osc.conf._boolean_opts:
            if opt not in config:
                continue
            self.assertIsInstance(config[opt], bool, msg=f"option: '{opt}'")

    def test_int_opts_defaults(self):
        config = osc.conf.config
        for opt in osc.conf._integer_opts:
            if opt not in config:
                continue
            self.assertIsInstance(config[opt], int, msg=f"option: '{opt}'")

    def test_bool_opts(self):
        oscrc = os.path.join(self._get_fixtures_dir(), "oscrc")
        osc.conf.get_config(override_conffile=oscrc, override_no_keyring=True)
        config = osc.conf.config
        for opt in osc.conf._boolean_opts:
            if opt not in config:
                continue
            self.assertIsInstance(config[opt], bool, msg=f"option: '{opt}'")

    def test_int_opts(self):
        oscrc = os.path.join(self._get_fixtures_dir(), "oscrc")
        osc.conf.get_config(override_conffile=oscrc, override_no_keyring=True)
        config = osc.conf.config
        for opt in osc.conf._integer_opts:
            if opt not in config:
                continue
            self.assertIsInstance(config[opt], int, msg=f"option: '{opt}'")


if __name__ == "__main__":
    unittest.main()
