# Twitter Account Details

This document provides an overview of the `account_details` functionality, usage instructions, and examples.

## Overview

The `account_details` function retrieves the authenticated Twitter (X) user account details. It uses the `tweepy` library to interact with the Twitter API and fetch the account details of the authenticated user.

## Usage Instructions

### Prerequisites

- Python 3.10 or higher
- `tweepy` library installed
- Twitter (X) App Developer Keys

### Installation

To install the required dependencies, run:

```bash
pip install tweepy
```

### Environment Setup

Set the following environment variables:

```bash
export TWITTER_API_KEY=<your-api-key>
export TWITTER_API_SECRET=<your-api-secret>
export TWITTER_ACCESS_TOKEN=<your-access-token>
export TWITTER_ACCESS_TOKEN_SECRET=<your-access-token-secret>
export TWITTER_BEARER_TOKEN=<your-bearer-token>
```

### Function Usage

To use the `account_details` function, follow these steps:

1. Import the necessary modules and create a `tweepy.Client` instance:

```python
import tweepy
from cdp_agentkit_core.actions.social.twitter.account_details import account_details

client = tweepy.Client(bearer_token="YOUR_BEARER_TOKEN")
```

2. Call the `account_details` function with the `client` instance:

```python
result = account_details(client)
print(result)
```

## Examples

### Example 1: Successful Retrieval of Account Details

```python
import tweepy
from cdp_agentkit_core.actions.social.twitter.account_details import account_details

client = tweepy.Client(bearer_token="YOUR_BEARER_TOKEN")
result = account_details(client)
print(result)
```

Expected output:

```
Successfully retrieved authenticated user account details:
{"data": {"id": "123456789", "name": "Test User", "username": "testuser", "url": "https://x.com/testuser"}}
```

### Example 2: Error Handling

```python
import tweepy
from cdp_agentkit_core.actions.social.twitter.account_details import account_details

client = tweepy.Client(bearer_token="INVALID_BEARER_TOKEN")
result = account_details(client)
print(result)
```

Expected output:

```
Error retrieving authenticated user account details:
401 Unauthorized
```
