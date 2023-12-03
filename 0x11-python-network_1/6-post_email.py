#!/usr/bin/python3
"""POST request using requests package - 2"""
import requests
from sys import argv

if __name__ == "__main__":
    hostname = argv[1]
    email = {'email': argv[2], }
    request = requests.post(hostname, data=email)
    print(request.text)
