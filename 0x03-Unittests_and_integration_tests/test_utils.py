#!/usr/bin/env python3
"""
this module parametruzes given functions and test for expected output
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


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
