#!/usr/bin/python3


import unittest

from osc.obs_api.xmlmodel import AttributeField
from osc.obs_api.xmlmodel import Model


class XMLModelTest(unittest.TestCase):
    def test_field_order(self):

        class Model1(Model):
            TAG_NAME = "foo"
            a = AttributeField(name="A")
            b = AttributeField(name="B")

        class Model2(Model1):
            TAG_NAME = "bar"
            # delete the 'a' field
            a = None
            b = AttributeField(name="B")

        class Model3(Model2):
            TAG_NAME = "baz"
            c = AttributeField(name="C")
            # bring the field 'a' back; it's going to be listed first according to the original definition
            a = AttributeField(name="A")
            d = AttributeField(name="D")

        m1 = Model1()
        expected = ["a", "b"]
        actual = [name for name, _ in m1.iter_field_names_objects()]
        self.assertEqual(actual, expected)

        m2 = Model2()
        expected = ["b"]
        actual = [name for name, _ in m2.iter_field_names_objects()]
        self.assertEqual(actual, expected)

        m3 = Model3()
        expected = ["a", "b", "c", "d"]
        actual = [name for name, _ in m3.iter_field_names_objects()]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
