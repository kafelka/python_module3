import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.calc = Calculator()
        self.assertEqual(6.5, self.calc.add(3,3.5))
    def test_subtr(self):
        self.calc = Calculator()
        self.assertEqual(-1, self.calc.subtract(2,3))
    def test_divide(self):
        self.calc = Calculator()
        self.assertEqual(1, self.calc.divide(1,1))
    def test_multiply(self):
        self.calc = Calculator()
        self.assertEqual(6, self.calc.multiply(2,3))
#    def test_calc_returns_error_msg_if_both_args_not_numbers(self):
#        self.calc = Calculator()
#        self.assertRaises(ValueError, self.calc.add, "two", "three")
#    def test_calc_returns_error_if_x_arg_not_number(self):
#        self.calc = Calculator()
#        self.assertRaises(ValueError, self.calc.add, "two", 3)
#    def test_calc_returns_error_if_y_arg_not_number(self):
#        self.calc = Calculator()
#        self.assertRaises(ValueError, self.calc.add, 2, "three")
    
if __name__ == "__main__":
    unittest.main()
    