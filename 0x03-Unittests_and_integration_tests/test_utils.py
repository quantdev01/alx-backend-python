#!/usr/bin/env python3
import utils
import unittest
from parameterized import parameterized
from unittest.mock import Mock
from unittest.mock import patch
from utils import memoize
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


class TestClass:
    """
    Test class
    """
    def a_method(self):
        """
        a method
        """
        return 42

    @memoize
    def a_property(self):
        """A property"""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """
    class test using memoize
    """
    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """
        memoize funtion usage
        """
        mock_a_method.return_value = 42

        test_instance = TestClass()
        result1 = test_instance.a_property
        result2 = test_instance.a_property

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        mock_a_method.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
