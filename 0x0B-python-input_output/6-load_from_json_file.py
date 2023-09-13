#!/usr/bin/python3
"""Task: 6. Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """create object from a JSON file"""
    with open(filename) as file:
        return json.load(file)
