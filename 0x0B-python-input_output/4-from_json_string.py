#!/usr/bin/python3
"""Task: 4. From JSON string to Object"""
import json


def from_json_string(my_str):
    """Deserialize JSON formatted str to a Python object."""
    return json.loads(my_str)
