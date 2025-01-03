# This file is not related to Coinbase API withdrawals.
# It is focused on testing Twitter account details.

from unittest.mock import patch

import pytest
import tweepy

from cdp_agentkit_core.actions.social.twitter.account_details import (
    AccountDetailsInput,
    account_details,
)

MOCK_USER_DETAILS = {
    "data": {
        "id": "1853889445319331840",
        "name": "CDP AgentKit",
        "username": "CDPAgentKit",
        "url": "https://x.com/CDPAgentKit",
    }
}


def test_account_details_input_model_valid():
    """Test that AccountDetailsInput accepts valid parameters."""
    input_model = AccountDetailsInput()

    assert isinstance(input_model, AccountDetailsInput)


def test_account_details_success():
    """Test successful retrieval of account details with valid parameters."""
    mock_client = patch("tweepy.Client.get_me", return_value=MOCK_USER_DETAILS)

    with mock_client as mock_get_me:
        action_response = account_details(mock_client)

        expected_response = f"Successfully retrieved authenticated user account details:\n{MOCK_USER_DETAILS}"
        assert action_response == expected_response
        mock_get_me.assert_called_once_with()


def test_account_details_api_error():
    """Test account_details when API error occurs."""
    mock_client = patch("tweepy.Client.get_me", side_effect=tweepy.errors.TweepyException("API error"))

    with mock_client as mock_get_me:
        action_response = account_details(mock_client)

        expected_response = "Error retrieving authenticated user account details:\nAPI error"
        assert action_response == expected_response
        mock_get_me.assert_called_once_with()
