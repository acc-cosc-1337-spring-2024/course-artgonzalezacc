import unittest

from src.examples.h_strings.strings import concat_string, concat_string_w_plus_equal, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_string_concatenation(self):
        self.assertEqual(concat_string("Python", "is cool!"), "Pythonis cool!")

    def test_string_concat_w_plus_equal(self):
        self.assertEqual(concat_string_w_plus_equal("C++ ", "cosc 1337"), "C++ cosc 1337")
        

