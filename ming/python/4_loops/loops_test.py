#!/bin/python3

import unittest

from loops import square


class TestSquare(unittest.TestCase):

    def square_base_test(self, num, expected_outcome):
        result = square(num)
        self.assertEqual(result, expected_outcome)

    def test_negative_num(self):
        self.square_base_test(-1, 1)

    def test_zero(self):
        self.square_base_test(0, 0)

    def test_one(self):
        self.square_base_test(1, 1)

    def test_five(self):
        self.square_base_test(5, 25)

    def test_ten(self):
        self.square_base_test(10, 100)


if __name__ == '__main__':
    unittest.main()
