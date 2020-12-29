#!/bin/python3

import unittest

from arithmetic_operators import add, minus, times

class TestAdd(unittest.TestCase):

    def test_add_1(self):
        result = add(5, 3)
        self.assertEqual(result, 8)

    def test_add_2(self):
        result = add(666, 43)
        self.assertEqual(result, 709)
    
    def test_add_3(self):
        result = add(1, 2)
        self.assertEqual(result, 3)


class TestMinus(unittest.TestCase):

    def test_minus_1(self):
        result = minus(5, 3)
        self.assertEqual(result, 2)
    
    def test_minus_2(self):
        result = minus(666, 43)
        self.assertEqual(result, 623)

    def test_minus_3(self):
        result = minus(1, 2)
        self.assertEqual(result, -1)


class TestTimes(unittest.TestCase):
    def test_times_1(self):
        result = times(5, 3)
        self.assertEqual(result, 15)
    
    def test_times_2(self):
        result = times(666, 43)
        self.assertEqual(result, 28638)

    def test_times_3(self):
        result = times(1, 2)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
