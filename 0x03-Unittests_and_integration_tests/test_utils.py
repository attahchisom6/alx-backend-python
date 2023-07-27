#!/usr/bin/env python3
"""
this module parametruzes given functions and test for expected output
"""
import unittest
from utils import access_nested_map, get_json
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
    def test_access_nested_map_exception(self, nested_map, path, expected_output):
        """
        test key error, then raise exceptions wen seen
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), str(expected_output))

class TestGetJson(unittest.TestCase):
    """
    This will test the get_json function from utils
    to see if it returns the expected output
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, payload: dict) -> bool:
        with patch('utils.requests.get') as mock_get:
            mock_response = mock_get.return_value
            mock_in_json = mock_response.json()
            mock_in_json.returned_value = payload
            self.assertEqual(get_json(url), payload)
