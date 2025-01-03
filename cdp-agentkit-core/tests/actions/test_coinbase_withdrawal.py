import requests
import requests_mock
import pytest
from cdp_agentkit_core.actions.coinbase_withdrawal import (
    coinbase_withdrawal,
    commit_withdrawal,
    get_withdrawal_status,
)

@pytest.fixture
def mock_requests():
    with requests_mock.Mocker() as m:
        yield m

def test_coinbase_withdrawal(mock_requests):
    account_id = "82de7fcd-db72-5085-8ceb-bee19303080b"
    amount = "10"
    currency = "USD"
    payment_method = "83562370-3e5c-51db-87da-752af5ab9559"
    bearer_token = "abd90df5f27a7b170cd775abf89d632b350b7c1c9d53e08b340cd9832ce52c2c"

    mock_response = {
        "data": {
            "id": "67e0eaec-07d7-54c4-a72c-2e92826897df",
            "status": "created",
            "payment_method": {
                "id": "83562370-3e5c-51db-87da-752af5ab9559",
                "resource": "payment_method",
                "resource_path": "/v2/payment-methods/83562370-3e5c-51db-87da-752af5ab9559"
            },
            "transaction": {
                "id": "441b9494-b3f0-5b98-b9b0-4d82c21c252a",
                "resource": "transaction",
                "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede/transactions/441b9494-b3f0-5b98-b9b0-4d82c21c252a"
            },
            "amount": {
                "amount": "10.00",
                "currency": "USD"
            },
            "subtotal": {
                "amount": "10.00",
                "currency": "USD"
            },
            "created_at": "2015-01-31T20:49:02Z",
            "updated_at": "2015-02-11T16:54:02-08:00",
            "resource": "withdrawal",
            "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede/withdrawals/67e0eaec-07d7-54c4-a72c-2e92826897df",
            "committed": True,
            "fee": {
                "amount": "0.00",
                "currency": "USD"
            },
            "payout_at": "2015-02-18T16:54:00-08:00"
        }
    }

    mock_requests.post(
        f"https://api.coinbase.com/v2/accounts/{account_id}/withdrawals",
        json=mock_response
    )

    response = coinbase_withdrawal(account_id, amount, currency, payment_method, bearer_token)
    assert response == mock_response

def test_commit_withdrawal(mock_requests):
    account_id = "82de7fcd-db72-5085-8ceb-bee19303080b"
    withdrawal_id = "a333743d-184a-5b5b-abe8-11612fc44ab5"
    bearer_token = "abd90df5f27a7b170cd775abf89d632b350b7c1c9d53e08b340cd9832ce52c2c"

    mock_response = {
        "data": {
            "id": "67e0eaec-07d7-54c4-a72c-2e92826897df",
            "status": "created",
            "payment_method": {
                "id": "83562370-3e5c-51db-87da-752af5ab9559",
                "resource": "payment_method",
                "resource_path": "/v2/payment-methods/83562370-3e5c-51db-87da-752af5ab9559"
            },
            "transaction": {
                "id": "441b9494-b3f0-5b98-b9b0-4d82c21c252a",
                "resource": "transaction",
                "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede/transactions/441b9494-b3f0-5b98-b9b0-4d82c21c252a"
            },
            "amount": {
                "amount": "10.00",
                "currency": "USD"
            },
            "subtotal": {
                "amount": "10.00",
                "currency": "USD"
            },
            "created_at": "2015-01-31T20:49:02Z",
            "updated_at": "2015-02-11T16:54:02-08:00",
            "resource": "withdrawal",
            "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede/withdrawals/67e0eaec-07d7-54c4-a72c-2e92826897df",
            "committed": True,
            "fee": {
                "amount": "0.00",
                "currency": "USD"
            },
            "payout_at": "2015-02-18T16:54:00-08:00"
        }
    }

    mock_requests.post(
        f"https://api.coinbase.com/v2/accounts/{account_id}/withdrawals/{withdrawal_id}/commit",
        json=mock_response
    )

    response = commit_withdrawal(account_id, withdrawal_id, bearer_token)
    assert response == mock_response

def test_get_withdrawal_status(mock_requests):
    account_id = "2bbf394c-193b-5b2a-9155-3b4732659ede"
    withdrawal_id = "67e0eaec-07d7-54c4-a72c-2e92826897df"
    bearer_token = "abd90df5f27a7b170cd775abf89d632b350b7c1c9d53e08b340cd9832ce52c2c"

    mock_response = {
        "data": {
            "id": "67e0eaec-07d7-54c4-a72c-2e92826897df",
            "status": "completed",
            "payment_method": {
                "id": "83562370-3e5c-51db-87da-752af5ab9559",
                "resource": "payment_method",
                "resource_path": "/v2/payment-methods/83562370-3e5c-51db-87da-752af5ab9559"
            },
            "transaction": {
                "id": "441b9494-b3f0-5b98-b9b0-4d82c21c252a",
                "resource": "transaction",
                "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede/transactions/441b9494-b3f0-5b98-b9b0-4d82c21c252a"
            },
            "amount": {
                "amount": "10.00",
                "currency": "USD"
            },
            "subtotal": {
                "amount": "10.00",
                "currency": "USD"
            },
            "created_at": "2015-01-31T20:49:02Z",
            "updated_at": "2015-02-11T16:54:02-08:00",
            "resource": "withdrawal",
            "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede/withdrawals/67e0eaec-07d7-54c4-a72c-2e92826897df",
            "committed": True,
            "fee": {
                "amount": "0.00",
                "currency": "USD"
            },
            "payout_at": "2015-02-18T16:54:00-08:00"
        }
    }

    mock_requests.get(
        f"https://api.coinbase.com/v2/accounts/{account_id}/withdrawals/{withdrawal_id}",
        json=mock_response
    )

    response = get_withdrawal_status(account_id, withdrawal_id, bearer_token)
    assert response == mock_response
