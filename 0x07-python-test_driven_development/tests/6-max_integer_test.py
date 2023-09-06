#!/usr/bin/python3
"""Creating unittests for def max_integer(list=[])"""


import unittest
max_integer = __import__('6-max_integer_test').max_integer


class TestMaxInteger(unittest.TestCase):

    """define unittest for max_integer([])"""
    def test_ordered_list(self):
        """Tests an ordered list of integers"""
        ordered_list = [2, 4, 6, 8]
        self.assertEqual(max_integer(ordered_list), 8)

    def test_unordered_list(self):
        """Tests an unordered list of integers"""
        unordered_list = [15, 0, 30, 5]
        self.assertEqual(max_integer(unordered_list), 30)

    def test_max_at_start(self):
        """Tests a descending list of integers"""
        max_at_start = [8, 6, 4, 2]
        self.assertEqual(max_integer(max_at_start), 8)

    def test_empty_list(self):
        """Tests an empty list of integers"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_integer_list(self):
        """Tests a list of one integer"""
        one_integer = [8]
        self.assertEqual(max_integer(one_integer), 8)


if __name__ == '__main__':
    unittest.main()
