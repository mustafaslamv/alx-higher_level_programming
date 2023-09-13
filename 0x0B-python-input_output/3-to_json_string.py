#!/usr/bin/python3
"""Task: 3. To JSON string"""
import json


def to_json_string(my_obj):
    """function returns the JSON of an object as str (serialization)"""
    return json.dumps(my_obj)
