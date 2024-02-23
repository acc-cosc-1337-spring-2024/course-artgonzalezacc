import unittest

from src.examples.h_strings.strings import concat_string, concat_string_w_plus_equal, string_params, string_return_value, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_string_concatenation(self):
        self.assertEqual(concat_string("Python", "is cool!"), "Pythonis cool!")

    def test_string_concat_w_plus_equal(self):
        self.assertEqual(concat_string_w_plus_equal("C++ ", "cosc 1337"), "C++ cosc 1337")

    def test_string_params_modify(self):
        lang = "C++"
        string_params(lang)
        self.assertEqual(lang, "C++")
    
    def test_string_return_value(self):
        lang = "C++"
        lang = string_return_value(lang) #lang is overwritten with the value of C++, 
        self.assertEqual(lang, "Python")
        

