#!/usr/bin/python3
"""GET request using requests package"""
import requests
from sys import argv

if __name__ == "__main__":
    hostname = argv[1]
    request = requests.get(hostname)
    code = request.status_code
    if (code >= 400):
        print(f"Error code: {code}")
    else:
        print(request.text)
