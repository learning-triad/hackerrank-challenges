#!/bin/python3

import unittest

from loops import generator, square

class TestGenerator(unittest.TestCase):

    def generator_base_test(self, num, expected_outcome):
        result = list(generator(num))
        self.assertEqual(result, expected_outcome)

    def test_negative_num(self):
        self.generator_base_test(-1, [])

    def test_zero(self):
        self.generator_base_test(0, [])

    def test_one(self):
        self.generator_base_test(1, [0])

    def test_five(self):
        self.generator_base_test(5, [0, 1, 4, 9, 16])

    def test_ten(self):
        self.generator_base_test(10,
            [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])


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
