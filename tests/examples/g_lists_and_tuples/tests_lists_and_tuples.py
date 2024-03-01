import unittest

from src.examples.g_lists_and_tuples.lists import find_item_in_list, list_parameter, list_parameter_return, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_list_parameter_works_with_one_list(self):
        even_numbers = [2,4,6,8,10]
        expected_list = [0,4,6,8,10]
        
        list_parameter(even_numbers)

        self.assertEqual(even_numbers, expected_list)

    def test_list_parameter_return_works_with_one_list(self):
        even_numbers = [2,4,6,8,10]
        expected_list = [0,4,6,8,10]

        list_parameter_return(even_numbers)

        self.assertEqual(even_numbers, expected_list)

    def tests_list_parameter_return_works_with_one_list_capture_return_value(self):
        even_numbers = [2,4,6,8,10]
        expected_list = [0,4,6,8,10]

        return_list = list_parameter_return(even_numbers)

        self.assertEqual(return_list, even_numbers)

    def test_find_item_in_list(self):
        prods = ["V475", "F987", "Q143", "R688"]
        result = find_item_in_list("Q143", prods)

        self.assertEqual(result, True)

    def test_find_item_not_in_list(self):
        prods = ["V475", "F987", "Q143", "R688"]
        result = find_item_in_list("q143", prods)

        self.assertEqual(result, False)

    def test_append_item_to_list(self):
        names = []
        names.append("Python")

        self.assertEqual(names, ["Python"])
