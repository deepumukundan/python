import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 2), 3)
        self.assertEqual(self.calculator.add(-1, 2), 1)
        self.assertEqual(self.calculator.add(-1, -2), -3)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(1, 2), -1)
        self.assertEqual(self.calculator.subtract(-1, 2), -3)
        self.assertEqual(self.calculator.subtract(-1, -2), 1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(1, 2), 2)
        self.assertEqual(self.calculator.multiply(-1, 2), -2)
        self.assertEqual(self.calculator.multiply(-1, -2), 2)