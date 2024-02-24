import unittest

from src.examples.h_strings.strings import concat_string, concat_string_w_plus_equal, get_length_of_string, get_number_of_ch_in_string, string_params, string_return_value, test_config

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

    def test_string_in_keyword(self):
        text = "Four score and seven years ago"
        is_in = 'seven' in text

        self.assertEqual(is_in, True)

    def test_string_in_keyword_2(self):
        text = "Four score and seven years ago"
        is_in = 'Seven' in text
        self.assertEqual(is_in, False)

    def test_get_length_w_len(self):
        lang = "Python"
        length = get_length_of_string(lang)

        self.assertEqual(length, 6)
        
    def test_get_number_of_ch_in_string(self):
        text = "Python"
        count = get_number_of_ch_in_string(text, 't')

        self.assertEqual(count, 1)

    def test_string_isalnum(self):
        text = "C++"
        self.assertEqual(text.isalnum(), False)

    def test_string_isdigit(self):
        val = "123"
        self.assertEqual(val.isdigit(), True)

    def test_string_isupper(self):
        val = "PYTHON"
        self.assertEqual(val.isupper(), True)

    def test_string_to_lower(self):
        val = "PYTHON"
        val = val.lower()
        self.assertEqual(val, "python")

    def test_string_rstrip(self):
        val = "Python  "
        val = val.rstrip()

        self.assertEqual(val, "Python")

    def test_string_endswith(self):
        val = "file.txt"

        self.assertEqual(val.endswith('.txt'), True)

    def test_string_replace(self):
        val = "Python"
        val = val.replace('Py', 'pi')
        self.assertEqual(val, 'pithon')

    def test_string_repetition_operator(self):
        val = 'w' * 5
        self.assertEqual(val, 'wwwww')

    def test_split_string(self):
        text = "Four score and seven years ago"
        split_text = text.split()

        self.assertEqual(split_text, ['Four', 'score', 'and', 'seven', 'years', 'ago'])


