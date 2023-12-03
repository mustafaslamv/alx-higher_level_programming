#!/usr/bin/python3
"""Python script that sends HTTP request using urllib - 2"""
from urllib import request
from sys import argv

if __name__ == "__main__":
    hostname = argv[1]
    req = request.Request(hostname)
    with request.urlopen(req) as response:
        content = response.info()
        xRequestId = content.get('X-Request-Id')
        print(xRequestId)
