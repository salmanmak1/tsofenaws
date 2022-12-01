#!/usr/bin/python3

import unittest
from importlib.machinery import SourceFileLoader
#from ..project.code.calculator import calc, sum
calculator=SourceFileLoader('calculator','../code/calculator.py').load_module()
from calculator import calc, sum

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.a = 600
        self.b = 100

    def test_add(self):
        calc1 = calc(self.a, self.b)
        self.assertEqual(calc1.add(), 700)

    def test_sub(self):
        calc1 = calc(self.a, self.b)
        self.assertEqual(calc1.sub(), 500)

    def test_mul(self):
        calc1 = calc(self.a, self.b)
        self.assertEqual(calc1.mul(), 60000)

    def test_div(self):
        calc1 = calc(self.a, self.b)
        self.assertEqual(calc1.div(), 6)

class TestSum(unittest.TestCase):
    def test_sum_function(self):
        self.assertEqual(sum([1,2,3,4,5]), 15)

if __name__ == '__main__':
    unittest.main(verbosity=2)
