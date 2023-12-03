#!/usr/bin/python3
"""POST request using requests package"""
import requests
from sys import argv

if __name__ == "__main__":
    hostname = "http://0.0.0.0:5000/search_user"
    q = argv[1] if len(argv) >= 2 else ""
    response = requests.post(hostname, {'q': q})

    try:
        dic = response.json()
    except ValueError:
        dic = None

    if dic is None:
        print("Not a valid JSON")
    elif not dic:
        print("No result")
    else:
        id = dic.get('id')
        name = dic.get('name')
        print(f"[{id}] {name}")
