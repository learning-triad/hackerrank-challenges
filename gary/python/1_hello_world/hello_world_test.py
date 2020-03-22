#!/bin/python3

import unittest

from hello_world import return_str


class TestReturnStr(unittest.TestCase):
    def test_return_hi(self):
        result = return_str("hi")
        self.assertEqual(result, "hi")

    def test_return_hello_world(self):
        result = return_str("Hello, World!")
        self.assertEqual(result, "Hello, World!")


if __name__ == '__main__':
    unittest.main()
