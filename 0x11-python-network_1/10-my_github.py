#!/usr/bin/python3
"""POST request using requests package"""
import requests
from sys import argv

if __name__ == "__main__":
    hostname = "https://api.github.com/user"
    username = argv[1]
    password_token = argv[2]
    header_values = {
        'Authorization': f'Bearer {password_token}',
        'Accept': 'application/vnd.github.v3+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    response = requests.get(hostname, headers=header_values)
    print(response.json().get("id"))
