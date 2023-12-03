#!/usr/bin/python3
"""Python script that sends HTTP request using urllib - 4"""
from urllib import request
from urllib import error
from sys import argv

if __name__ == "__main__":
    hostname = argv[1]
    try:
        req = request.Request(hostname)
        with request.urlopen(req) as response:
            content = response.read().decode("UTF-8")
            print(content)
    except error.HTTPError as error:
        print(f"Error code: {error.code}")
