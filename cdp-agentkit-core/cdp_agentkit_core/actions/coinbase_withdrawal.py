import requests

def coinbase_withdrawal(account_id: str, amount: str, currency: str, payment_method: str, bearer_token: str) -> dict:
    url = f"https://api.coinbase.com/v2/accounts/{account_id}/withdrawals"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    data = {
        "amount": amount,
        "currency": currency,
        "payment_method": payment_method
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def commit_withdrawal(account_id: str, withdrawal_id: str, bearer_token: str) -> dict:
    url = f"https://api.coinbase.com/v2/accounts/{account_id}/withdrawals/{withdrawal_id}/commit"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers)
    return response.json()

def get_withdrawal_status(account_id: str, withdrawal_id: str, bearer_token: str) -> dict:
    url = f"https://api.coinbase.com/v2/accounts/{account_id}/withdrawals/{withdrawal_id}"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()
