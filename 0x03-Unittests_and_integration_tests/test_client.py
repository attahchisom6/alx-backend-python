#!/usr/bin/env python3
"""
s module to test side,  all the functions from clients
are tested for a proper output here
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient as github_org
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """
    class to test if the output defined from a github api
    is correctly defined by the GithubOrgClient class
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    # we proceed to mock get_json from client module so that no actual
    # http request is made
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        this will test if an api endpoint correctly
        returns the expected value
        """
        expected_url = "https://api.github.com/orgs/{}".format(org_name)
        mock_get_json.return_value = {"name": org_name}

        # client module has bn mocked to prevent actual http request
        mocked_client = github_org(org_name)
        mocked_output = mocked_client.org

        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(mocked_output.get("name"), org_name)

    def test_public_repos_url(self):
        """
        test the output of the _public_repo _url method
        """
        # note: github_org is an alias for GitOrgClient
        with patch.object(
                github_org, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "abc"}
            mocked_output = mock_org.return_value

            github_client = github_org("abc")
            actual_output = github_client._public_repos_url
            self.assertEqual(actual_output, mocked_output.get("repos_url"))
