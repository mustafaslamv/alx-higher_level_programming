#!/usr/bin/python3
"""GET request using requests package - 2"""
import requests
from sys import argv

if __name__ == "__main__":
    hostname = argv[1]
    request = requests.get(hostname)
    XRequestId = request.headers.get("X-Request-Id")
    print(XRequestId)
