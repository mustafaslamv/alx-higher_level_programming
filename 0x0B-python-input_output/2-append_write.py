#!/usr/bin/python3
"""Task: 2. Append to a file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file"""
    with open(filename, "a", encoding="UTF8") as file:
        written = file.write(text)
    return written
