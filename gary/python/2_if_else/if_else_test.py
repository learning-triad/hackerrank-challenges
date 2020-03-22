#!/bin/python3

import unittest

from if_else import check_weirdness


class TestCheckWeirdness(unittest.TestCase):
    def test_odd_1(self):
        result = check_weirdness(1)
        self.assertEqual(result, "Weird")

    def test_odd_2_to_5(self):
        result = check_weirdness(3)
        self.assertEqual(result, "Weird")

    def test_odd_6_to_20(self):
        result = check_weirdness(19)
        self.assertEqual(result, "Weird")

    def test_odd_gt_than_20(self):
        result = check_weirdness(23)
        self.assertEqual(result, "Weird")

    def test_even_2_to_5(self):
        result = check_weirdness(4)
        self.assertEqual(result, "Not Weird")

    def test_even_6_to_20(self):
        result = check_weirdness(10)
        self.assertEqual(result, "Weird")

    def test_even_gt_than_20(self):
        result = check_weirdness(22)
        self.assertEqual(result, "Not Weird")

    def test_less_than_1(self):
        result = check_weirdness(-1)
        self.assertEqual(result, "Not Applicable")

    def test_gt_than_100(self):
        result = check_weirdness(101)
        self.assertEqual(result, "Not Applicable")


if __name__ == '__main__':
    unittest.main()
