#!/usr/bin/env python3
import utils
import unittest
from parameterized import parameterized
"""
Documented the lib this will be testing cases
"""


class TestAccessNestedMap(unittest.TestCase):
    """
    Class for testing the nested Map result
    """
    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
        ])
    def test_access_nested_map(self, a, b, expect):
        """
        my function to return assertEqual
        """
        self.assertEqual(utils.access_nested_map(a, b), expect)

    @parameterized.expand([
        ({}, "a", KeyError),
        ({"a": 1}, ["a", "b"], KeyError),
        ])
    def test_access_nested_map_exception(self, a, b, expect):
        """
        Raises an exception of KeyError
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(a, b)


if __name__ == '__main__':
    unittest.main()
