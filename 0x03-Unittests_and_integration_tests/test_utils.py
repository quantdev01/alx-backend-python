#!/usr/bin/env python3
import utils
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
        ])
    def test_access_nested_map(self, a, b, expect):
        self.assertEqual(utils.access_nested_map(a, b), expect)


if __name__ == '__main__':
    unittest.main()
