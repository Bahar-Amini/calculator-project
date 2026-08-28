import unittest

from operation import *
from validator import Validator


class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(Addition().execute(2.5, 10), 12.5)
        self.assertEqual(Addition().execute(1, -1), 0)
        self.assertEqual(Addition().execute(5, 4), 9)

    def test_subtract(self):
        self.assertEqual(Subtraction().execute(10, 5), 5)
        self.assertEqual(Subtraction().execute(10, -5), 15)
        self.assertEqual(Subtraction().execute(-5, 10), -15)
        self.assertEqual(Subtraction().execute(5, 10.5), -5.5)

    def test_divide(self):
        self.assertEqual(Division().execute(10, 2), 5)
        self.assertEqual(Division().execute(10, -2), -5)
        self.assertEqual(Division().execute(10, 2.5), 4)
        self.assertRaises(ZeroDivisionError, Division().execute, 10, 0)

    def test_multiply(self):
        self.assertEqual(Mulltiplication().execute(10, 2), 20)
        self.assertEqual(Mulltiplication().execute(10, -2), -20)
        self.assertEqual(Mulltiplication().execute(10, 2.5), 25)
        self.assertEqual(Mulltiplication().execute(10, 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Validator.validate_numbers("bb", "12")
            Validator.validate_operator("**")


if __name__ == "__main__":
    unittest.main()
