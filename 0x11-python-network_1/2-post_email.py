#!/usr/bin/python3
"""Python script that sends HTTP request using urllib - 2"""
from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    hostname = argv[1]
    email = {"email": argv[2]}
    email_decoded = parse.urlencode(email).encode('ascii')
    req = request.Request(hostname, data=email_decoded)
    with request.urlopen(req) as response:
        content = response.read().decode("UTF-8")
        print(content)
