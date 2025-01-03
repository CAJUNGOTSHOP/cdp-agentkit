import requests
import requests_mock
from cdp_agentkit_core.actions.coinbase_withdrawal import (
    coinbase_withdrawal,
    commit_withdrawal,
    get_withdrawal_status,
)

MOCK_ACCOUNT_ID = "mock_account_id"
MOCK_AMOUNT = "100.00"
MOCK_CURRENCY = "USD"
MOCK_PAYMENT_METHOD = "mock_payment_method"
MOCK_BEARER_TOKEN = "mock_bearer_token"
MOCK_WITHDRAWAL_ID = "mock_withdrawal_id"


def test_coinbase_withdrawal_success():
    """Test successful Coinbase withdrawal."""
    mock_response = {
        "data": {
            "id": MOCK_WITHDRAWAL_ID,
            "status": "completed",
            "amount": MOCK_AMOUNT,
            "currency": MOCK_CURRENCY,
        }
    }

    with requests_mock.Mocker() as m:
        m.post(f"https://api.coinbase.com/v2/accounts/{MOCK_ACCOUNT_ID}/withdrawals", json=mock_response)
        response = coinbase_withdrawal(MOCK_ACCOUNT_ID, MOCK_AMOUNT, MOCK_CURRENCY, MOCK_PAYMENT_METHOD, MOCK_BEARER_TOKEN)

        assert response == mock_response


def test_commit_withdrawal_success():
    """Test successful commit of Coinbase withdrawal."""
    mock_response = {
        "data": {
            "id": MOCK_WITHDRAWAL_ID,
            "status": "completed",
        }
    }

    with requests_mock.Mocker() as m:
        m.post(f"https://api.coinbase.com/v2/accounts/{MOCK_ACCOUNT_ID}/withdrawals/{MOCK_WITHDRAWAL_ID}/commit", json=mock_response)
        response = commit_withdrawal(MOCK_ACCOUNT_ID, MOCK_WITHDRAWAL_ID, MOCK_BEARER_TOKEN)

        assert response == mock_response


def test_get_withdrawal_status_success():
    """Test successful retrieval of Coinbase withdrawal status."""
    mock_response = {
        "data": {
            "id": MOCK_WITHDRAWAL_ID,
            "status": "completed",
            "amount": MOCK_AMOUNT,
            "currency": MOCK_CURRENCY,
        }
    }

    with requests_mock.Mocker() as m:
        m.get(f"https://api.coinbase.com/v2/accounts/{MOCK_ACCOUNT_ID}/withdrawals/{MOCK_WITHDRAWAL_ID}", json=mock_response)
        response = get_withdrawal_status(MOCK_ACCOUNT_ID, MOCK_WITHDRAWAL_ID, MOCK_BEARER_TOKEN)

        assert response == mock_response
