import unittest
from simple_calculator import SimpleCalculator

class TestSimplecalc(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(5, 3), 8)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6) 
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(7, 6), 42)
    def test_division(self): 
        self.assertEqual(self.calc.divide(20, 4), 5)
        self.assertIsNone(self.calc.divide(10, 0))    