#!/usr/bin/env python3
"""
this module parametruzes given functions and test for expected output
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        test the access_nested map function
        """
        actual_output = access_nested_map(nested_map, path)
        self.assertEqual(actual_output, expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError('a')),
        ({"a": 1}, ("a", "b",), KeyError('b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        test key error, then raise exceptions wen seen
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), str(expected))


class TestGetJson(unittest.TestCase):
    """
    This will test the get_json function from utils
    to see if it returns the expected output
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("test_utils.get_json")
    def test_get_json(self, url, test_payload, mock_get):
        mock_get.return_value = test_payload
        self.assertEqual(get_json(url),  test_payload)


class TestMemoize(unittest.TestCase):
    """ TESTCASE """
    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result is
        returned but a_method is on
        ly called once using assert_called_once
        """
        class TestClass:
            """ class """
            def a_method(self):
                """ method  """
                return 42

            @memoize
            def a_property(self):
                """ property """
                return self.a_method()
        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once
