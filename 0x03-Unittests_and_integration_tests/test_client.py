#!/usr/bin/env python3
"""
s module to test side,  all the functions from clients
are tested for a proper output here
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from utils import get_json
from fixtures import TEST_PAYLOAD


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
        mocked_client = GithubOrgClient(org_name)
        mocked_output = mocked_client.org

        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(mocked_output.get("name"), org_name)

    def test_public_repos_url(self):
        """
        test the output of the _public_repo _url method
        """
        # note: GithubOrgClient is an alias for GitOrgClient
        with patch.object(
                GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "abc"}
            mocked_output = mock_org.return_value

            github_client = GithubOrgClient("abc")
            actual_output = github_client._public_repos_url
            self.assertEqual(actual_output, mocked_output.get("repos_url"))

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        test if the public_repo method returns the desired list of
        public repositories
        """
        payloads = [
                {"name": "alx-repos"},
                {"name": "holberton-repos"},
                {"name": "bootcamp-repos"},
                {"name": "aws-repos"},
                {"name": "Azure"}
            ]

        mock_get_json.return_value = payloads

        with patch.object(
                GithubOrgClient,
                '_public_repos_url',
                new_callable=PropertyMock) as mock_list:
            mock_list.return_value = "coding-orgs"
            mocked_client = GithubOrgClient("SWE-Schools")
            mocked_output = mocked_client.public_repos()

            pub_repos = [repo["name"] for repo in payloads]
            self.assertEqual(pub_repos, mocked_output)

            mock_list.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": {"key": "other_license"}}, "other_license", True)])
    def test_has_license(self, repo, key, expected_output):
        actual_output = GithubOrgClient.has_license(repo, key)

        self.assertEqual(actual_output, expected_output)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    an integration test to check external http requests by
    mocking the requesting parameters(codes)
    """
    @classmethod
    def setUpClass(cls):
        """
        sets up or define objects in the integration test class
        """
        kwargs = {"return_value.json.side_effect":
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                      ]
                  }
        cls.get_patcher = patch("requests.get", **kwargs)
        cls.mock_get_json = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        reset the test parameters and objects wen we are through with it
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        an integration test to test the public repo module
        """
        mocked_client = GithubOrgClient("gameWorld.com")
        mocked_output = mocked_client.public_repos()

        self.assertEqual(mocked_output, self.expected_repos)
        self.assertEqual(mocked_client.repos_payload, self.repos_payload)
        self.assertEqual(mocked_client.org, self.org_payload)
        self.assertEqual(mocked_client.public_repos("wrong_license"), [])

    def test_public_repos_with_license(self):
        """
        test the public repo module with a given license
        """
        mocked_client = GithubOrgClient("GameWorld.com")
        mocked_output = mocked_client.public_repos

        self.assertEqual(mocked_output(), self.expected_repos)
        self.assertEqual(mocked_output("apache-2.0"), self.apache2_repos)
        self.assertEqual(mocked_output("wrong-licence"), [])
        self.mock_get_json.assert_called()
