import unittest

from src.examples.b_input_proc_output.input_process_output import add_values, floating_point_division, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_add_numbers(self):
        self.assertEqual(add_values(3, 4), 7)
        self.assertEqual(add_values(10.99, 1.50), 12.49)
        self.assertEqual(add_values("12.49", "1.50"), "12.491.50")

    def test_floating_point_division_1(self):
        self.assertEqual(floating_point_division(5, 2), 2.5)
        #self.assertEqual(floating_point_division(5, 2), 2.7)--make an assertion fail example

    def test_floating_point_division_2(self):
        self.assertEqual(floating_point_division(20, 8), 2.5)

