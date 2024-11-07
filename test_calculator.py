import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(6, 9), 15)
        self.assertEqual(self.calc.add(50, 12), 62)
        self.assertEqual(self.calc.subtract(8, 6), 2)
        self.assertEqual(self.calc.subtract(10, 200), -190)
        self.assertEqual(self.calc.multiply(7, 10), 70)
        self.assertEqual(self.calc.multiply(60, 70), 4200)
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(88, 77), 1)
        self.assertEqual(self.calc.modulo(89, 3), 2)
        self.assertEqual(self.calc.modulo(100, 20), 0)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()