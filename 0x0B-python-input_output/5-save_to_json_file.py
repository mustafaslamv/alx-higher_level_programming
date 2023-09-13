#!/usr/bin/python3
"""Task: 5. Save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """create JSON file from object"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
