#!/usr/bin/env python3
"""
s module to test side,  all the functions from clients
are tested for a proper output here
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
import GithubOrgClient as git_org
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """
    class to test if the output defined from a github api
    is correctly defined by the GithubOrgClient class
    """
    @parameterized.expand([
        (google),
        (abc)
    ])
    @patch("test_client.get_json")
    def test_org(org_name, mock_get_json):
        """
        this will test if an api endpoint correctly
        returns the expected value
        """
        payload = {"payload": true}
        mock_get_json.return_value = payload
        actual_output = git_org("org_name")
        self.assertEqual(actual_output, payload)
        mock_get_json.assert_called_once()
