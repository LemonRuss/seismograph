import unittest
from seismograph.ext.selenium.forms.group import *

class TestGroup(unittest.TestCase):

    def test_make_field(self):
        self.assertRaises(ValueError, lambda: make_field(int))
        self.assertEqual(type(make_field(FieldsGroup)), GroupContainer)