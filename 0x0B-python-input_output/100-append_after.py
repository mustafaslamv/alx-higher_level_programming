#!/usr/bin/python3
"""Task: 13. search and update"""


def append_after(filename="", search_string="", new_string=""):
    """append line after specific string"""

    result = ""
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            result += line
            if search_string in line:
                result += new_string
    with open(filename, "w") as file:
        file.write(result)
