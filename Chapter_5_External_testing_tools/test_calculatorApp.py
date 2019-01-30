import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(6, calc.add(3,3))
    def test_subtr(self):
        calc = Calculator()
        self.assertEqual(-1, calc.subtract(2,3))
    def test_divide(self):
        calc = Calculator()
        self.assertEqual(1, calc.divide(1,1))
    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(6, calc.multiply(2,3))
    def test_calc_returns_error_msg_if_both_args_not_numbers(self):
        calc = Calculator()
        self.assertRaises(ValueError, calc.add, "two", "three")
    
if __name__ == "__main__":
    unittest.main()
    