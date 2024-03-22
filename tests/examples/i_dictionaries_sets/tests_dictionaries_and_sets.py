import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_dictionary_key_access(self):
        prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
        self.assertEqual(prog_langs['C++'], '1979')

    def test_dictionary_find_key_with_in(self):
        prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
        self.assertEqual('C++' in prog_langs, True)
        self.assertEqual('c++' in prog_langs, False)

    def test_dictionary_find_key_with_not_in(self):
        prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
        self.assertEqual('C++' not in prog_langs, False)
        self.assertEqual('c++' not in prog_langs, True)

    def test_add_key_pair_to_dictionary(self):
        prog_langs = {}
        prog_langs['Python'] = '1996'

        self.assertEqual(prog_langs['Python'], '1996')

    def test_add_duplicate_key_pair_to_dictionary_overwrites_existing_key_value(self):
        prog_langs = {'C++':'1979'}
        prog_langs['C++'] = '1980'
        self.assertEqual(prog_langs['C++'], '1980')

    def test_add_key_pair_to_dictionary_key_case_sensitive(self):
        prog_langs = {'C++':'1979'}
        prog_langs['c++'] = '1980'
        self.assertEqual(prog_langs['C++'], '1979')
        self.assertEqual(prog_langs['c++'], '1980')
    
    def test_delete_key_pair_from_dictionary(self):
        prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
        del prog_langs['C#'] 
        self.assertEqual(prog_langs, {'C++':'1979', 'Java':'1992', 'Python':'1996'})


