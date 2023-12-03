#!/usr/bin/python3
import requests

request = requests.get("https://alx-intranet.hbtn.io/status")
decoded_response = request.text
print("Body response:")
print(f"\t- type: {type(decoded_response)}")
print(f"\t- content: {decoded_response}")
