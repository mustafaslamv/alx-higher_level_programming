#!/usr/bin/python3
"""Task: 4. From JSON string to Object"""
import json


def from_json_string(my_str):
    """function returns object represented by JSON string (deserialization)"""
    return json.loads(my_str)
