import unittest
from unittest.mock import patch, MagicMock
from cdp_agentkit_core.actions.social.twitter.account_details import account_details

class TestAccountDetails(unittest.TestCase):
    """Unit tests for the account_details function."""

    @patch('cdp_agentkit_core.actions.social.twitter.account_details.tweepy.Client')
    def test_account_details_success(self, MockClient):
        """Test successful retrieval of account details."""
        mock_client = MockClient.return_value
        mock_response = {
            'data': {
                'id': '123456789',
                'name': 'Test User',
                'username': 'testuser'
            }
        }
        mock_client.get_me.return_value = mock_response

        result = account_details(mock_client)
        expected_message = 'Successfully retrieved authenticated user account details:\n{"data": {"id": "123456789", "name": "Test User", "username": "testuser", "url": "https://x.com/testuser"}}'

        self.assertEqual(result, expected_message)

    @patch('cdp_agentkit_core.actions.social.twitter.account_details.tweepy.Client')
    def test_account_details_error(self, MockClient):
        """Test error handling in account_details function."""
        mock_client = MockClient.return_value
        mock_client.get_me.side_effect = Exception("Test error")

        result = account_details(mock_client)
        expected_message = 'Error retrieving authenticated user account details:\nTest error'

        self.assertEqual(result, expected_message)

    @patch('cdp_agentkit_core.actions.social.twitter.account_details.tweepy.Client')
    def test_account_details_invalid_input(self, MockClient):
        """Test handling of invalid input parameters."""
        mock_client = MockClient.return_value
        mock_client.get_me.side_effect = ValueError("Invalid input")

        result = account_details(mock_client)
        expected_message = 'Error retrieving authenticated user account details:\nInvalid input'

        self.assertEqual(result, expected_message)

    @patch('cdp_agentkit_core.actions.social.twitter.account_details.tweepy.Client')
    def test_account_details_unexpected_response_format(self, MockClient):
        """Test handling of unexpected response format from Twitter API."""
        mock_client = MockClient.return_value
        mock_response = {
            'unexpected_key': 'unexpected_value'
        }
        mock_client.get_me.return_value = mock_response

        result = account_details(mock_client)
        expected_message = 'Error retrieving authenticated user account details:\n\'data\''

        self.assertEqual(result, expected_message)

if __name__ == '__main__':
    unittest.main()
