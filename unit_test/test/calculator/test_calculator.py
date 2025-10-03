import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_Add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def testSubstract(self):
        self.assertEqual(self.calc.substract(2, 3), -1)