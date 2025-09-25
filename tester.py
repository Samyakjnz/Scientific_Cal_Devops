# test_calculator.py
import unittest
import math
from calculator import square_root, factorial, natural_log, power

class TestCalculatorFunctions(unittest.TestCase):
    def test_square_root(self):
        self.assertEqual(square_root(9), 3.0)
        self.assertIn("Error", square_root(-1))
        self.assertEqual(square_root(0), 0.0)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertIn("Error", factorial(5.5))
        self.assertIn("Error", factorial(-1))

    def test_natural_log(self):
        self.assertAlmostEqual(natural_log(math.e), 1.0)
        self.assertIn("Error", natural_log(0))
        self.assertIn("Error", natural_log(-5))

    def test_power(self):
        self.assertEqual(power(2, 3), 8.0)
        self.assertEqual(power(4, 0.5), 2.0)
        self.assertEqual(power(2, -2), 0.25)
        self.assertEqual(power(5, 0), 1.0)

if __name__ == '__main__':
    unittest.main()