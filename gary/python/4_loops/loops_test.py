#!/bin/python3

import unittest

from loops import generator, square

class TestGenerator(unittest.TestCase):

    def generator(self, num, expected_outcome):
        result = list(generator(num))
        self.assertEqual(result, expected_outcome)

    def test_negative_num(self):
        self.generator(-1, [])

    def test_zero(self):
        self.generator(0, [])

    def test_one(self):
        self.generator(1, [0])

    def test_five(self):
        self.generator(5, [0, 1, 4, 9, 16])

    def test_ten(self):
        self.generator(10,
            [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])


class TestSquare(unittest.TestCase):

    def square(self, num, expected_outcome):
        result = square(num)
        self.assertEqual(result, expected_outcome)

    def test_negative_num(self):
        self.square(-1, 1)

    def test_zero(self):
        self.square(0, 0)

    def test_one(self):
        self.square(1, 1)

    def test_five(self):
        self.square(5, 25)

    def test_ten(self):
        self.square(10, 100)


if __name__ == '__main__':
    unittest.main()
