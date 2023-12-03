#!/usr/bin/python3
"""POST request using requests package"""
import requests
from sys import argv

if __name__ == "__main__":
    hostname = "http://0.0.0.0:5000/search_user"
    q = argv[1] if len(argv) >= 2 else ""
    request = requests.post(hostname, {'q': q})
    dict = request.json()
    if not dict:
        print("No result")
    else:
        id = dict.get('id')
        name = dict.get('name')
        print(f"[{id}] {name}")
