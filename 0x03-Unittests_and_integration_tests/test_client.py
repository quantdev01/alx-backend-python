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


if __name__ == "__main__":
    unittest.main()
