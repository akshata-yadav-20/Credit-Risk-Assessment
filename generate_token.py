#!/usr/bin/env python3
"""
Generate GitHub Personal Access Token using the GitHub OAuth flow.
Note: This requires GitHub username and password (or 2FA code if enabled).
"""
import requests
import json
import subprocess
import sys

# GitHub credentials
username = 'akshata-yadav-20'
password = 'Akshata@7389'

# Step 1: Authenticate and create a token
auth_url = 'https://api.github.com/authorizations'
headers = {
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'Content-Type': 'application/json'
}

# Try to create a token using password
data = {
    'note': 'Credit Risk Assessment Repo Update',
    'scopes': ['repo', 'public_repo']
}

response = requests.post(auth_url, headers=headers, auth=(username, password), json=data)
print(f'Auth Status: {response.status_code}')

if response.status_code == 201:
    token = response.json()['token']
    print(f'Token created: {token[:10]}...')
    
    # Use token to update repository
    repo_url = 'https://api.github.com/repos/akshata-yadav-20/Credit-Risk-Assessment'
    update_headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'token {token}',
        'X-GitHub-Api-Version': '2022-11-28',
        'Content-Type': 'application/json'
    }
    
    update_data = {
        'homepage': 'https://akshata-yadav-20.github.io/Credit-Risk-Assessment/'
    }
    
    update_response = requests.patch(repo_url, headers=update_headers, json=update_data)
    print(f'Repo Update Status: {update_response.status_code}')
    if update_response.status_code == 200:
        print("✅ Repository updated successfully!")
        print(json.dumps(update_response.json(), indent=2))
    else:
        print("Failed to update repository:")
        print(json.dumps(update_response.json(), indent=2))
elif response.status_code == 401:
    print("Authentication failed - GitHub has deprecated password auth for API calls")
    print("\nManual setup required:")
    print("1. Generate a PAT at https://github.com/settings/tokens")
    print("2. Run update_repo.py with the token")
else:
    print(f"Unexpected response: {response.status_code}")
    print(json.dumps(response.json(), indent=2))