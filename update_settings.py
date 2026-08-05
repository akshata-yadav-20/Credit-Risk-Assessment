#!/usr/bin/env python3
"""
Update repository settings on GitHub.
"""
import requests
import json

# GitHub credentials (using token format)
token = input("Please enter your GitHub Personal Access Token: ")

# Repository details
repo_owner = 'akshata-yadav-20'
repo_name = 'Credit-Risk-Assessment'

# API endpoint
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}'

# Headers
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'token {token}',
    'X-GitHub-Api-Version': '2022-11-28',
    'Content-Type': 'application/json'
}

# Data to update
data = {
    'homepage': 'https://akshata-yadav-20.github.io/Credit-Risk-Assessment/'
}

# Make request
response = requests.patch(url, headers=headers, json=data)
print(f'Status Code: {response.status_code}')
if response.status_code == 200:
    print("✅ Repository updated successfully!")
    print(json.dumps(response.json(), indent=2))
else:
    print("Failed to update repository:")
    print(json.dumps(response.json(), indent=2))