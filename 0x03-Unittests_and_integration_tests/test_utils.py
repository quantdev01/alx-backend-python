#!/usr/bin/env python3
import utils
import unittest
from parameterized import parameterized
from unittest.mock import Mock
from unittest.mock import patch
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


class TestGetJson(unittest.TestCase):
    """
    This class test using Mock simulation
    """
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
        ])
    @patch('utils.requests.get')
    def test_get_json(self, website, expect, mock_get):
        """
        Get website using Mock()
        """
        mock_response = Mock()

        mock_response.json.return_value = expect

        mock_get.return_value = mock_response

        result = utils.get_json(website)

        mock_get.assert_called_once_with(website)

        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
