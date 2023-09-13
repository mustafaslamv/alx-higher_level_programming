#!/usr/bin/python3
import sys
import json

if __name__ == "__main__":
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__("6-load_from_json_file").load_from_json_file
    arguments = sys.argv[1:]
    try:
        data = load_from_json("add_item.json")
    except FileNotFoundError:
        data = []

    data.extend(arguments)
    save_to_json(data, "add_item.json")
