#!/usr/bin/python3
"""Task: 1. Write to a file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""
    with open(filename, "w", encoding="UTF8") as file:
        written = file.write(text)
    return written
