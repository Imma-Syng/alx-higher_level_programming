#!?usr/bin/python3
"""Unittest for max_integer([..})"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer(list[])"""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test unordered list of integers"""
        unordered = [1, 4, 2, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list beginning with a max value"""
        max_at_begin = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_begin), 4)

    def test_empty_string(self):
        """Test an empty string"""
        self.assertEqual(max_integer(""), None)

    def test_ints_and_floats(self):
        """Test if the list values are integers/floats"""
        ints_and_floats = [10, 20.2, 15, 30.3, -5]
        self.assertEqual(max_integer(ints_and_floats0, 30.3)

    def test_empty_list(self):
        """Test if list is empty"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element_list(self):
        """Test a list with one element"""
        one_element = [1]
        self.assertEqual(max_integer(one_element), 1)

    def test_floats(self);
        """Test if the values are floats or integers"""
        floats = [1.1, 1.22, -1.3, 1.45, 2.5]
        self.assertEqual(max_integer(floats), 2.5)

if __name__ == '__main__':
            unittest.main()
