#!/usr/bin/env python3
"""
Module docummentation
mod docu
"""


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient.org method."""

    @parameterized.expand([
        ("google",),
        ("abc",),
        ])
    @patch('client.get_json', return_value={
        "repos_url": "https://api.github.com/orgs/sample/repos"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Arrange: Create a GithubOrgClient instance for the given org_name
        client = GithubOrgClient(org_name)

        # Act: Call the org method (as a property, not a function)
        result = client.org  # org is memoized, access as a property

        # Assert: Ensure get_json is called once with the correct URL
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {
            "repos_url": "https://api.github.com/orgs/sample/repos"})


    def test_public_repos_url(self):
        """Test that GithubOrgClient._public_repos_url returns the correct URL based on the mocked org."""
        with patch('client.GithubOrgClient.org', new_callable=property) as mock_org:
            # Arrange: Set the return value for the mocked org property
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test_org/repos"}
            
            # Act: Create a GithubOrgClient instance and access _public_repos_url
            client = GithubOrgClient("test_org")
            result = client._public_repos_url  # Access the property
            
            # Assert: Ensure the result is what we expect
            self.assertEqual(result, "https://api.github.com/orgs/test_org/repos")


if __name__ == "__main__":
    unittest.main()
