#!/bin/python3

import unittest

from arithmetic_operators import add, minus, times


class TestAdd(unittest.TestCase):

    def add_base_test(self, num1, num2, expected_result):
        result = add(num1, num2)
        self.assertEqual(result, expected_result)

    def test_add_medium_numbers(self):
        self.add_base_test(5, 3, 8)

    def test_add_big_numbers(self):
        self.add_base_test(666, 43, 709)

    def test_add_small_numbers(self):
        self.add_base_test(1, 2, 3)

    def test_add_negative_numbers(self):
        self.add_base_test(-10, -20, -30)

    def test_add_mixed_numbers(self):
        self.add_base_test(-10, 20, 10)

    def test_add_zeros(self):
        self.add_base_test(0, 0, 0)

    def test_add_zero_number(self):
        self.add_base_test(0, 9999, 9999)


class TestMinus(unittest.TestCase):

    def minus_base_test(self, num1, num2, expected_result):
        result = minus(num1, num2)
        self.assertEqual(result, expected_result)

    def test_minus_medium_numbers(self):
        self.minus_base_test(5, 3, 2)

    def test_minus_big_numbers(self):
        self.minus_base_test(666, 43, 623)

    def test_minus_small_numbers(self):
        self.minus_base_test(3, 2, 1)

    def test_minus_negative_numbers(self):
        self.minus_base_test(-10, -20, 10)

    def test_minus_mixed_numbers(self):
        self.minus_base_test(-10, 20, -30)

    def test_minus_zeros(self):
        self.minus_base_test(0, 0, 0)

    def test_minus_zero_number(self):
        self.minus_base_test(0, 9999, -9999)


class TestTimes(unittest.TestCase):

    def times_base_test(self, num1, num2, expected_result):
        result = times(num1, num2)
        self.assertEqual(result, expected_result)

    def test_times_medium_numbers(self):
        self.times_base_test(5, 3, 15)

    def test_times_big_numbers(self):
        self.times_base_test(666, 43, 28638)

    def test_times_small_numbers(self):
        self.times_base_test(3, 2, 6)

    def test_times_negative_numbers(self):
        self.times_base_test(-10, -20, 200)

    def test_times_mixed_numbers(self):
        self.times_base_test(-10, 20, -200)

    def test_times_zeros(self):
        self.times_base_test(0, 0, 0)

    def test_times_zero_number(self):
        self.times_base_test(0, 9999, 0)


if __name__ == '__main__':
    unittest.main()
