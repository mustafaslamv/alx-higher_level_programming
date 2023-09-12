#!/usr/bin/python3
"""Task: 0.Read files"""


def read_file(filename=""):
    """function reads text file as UTF8 and prints it"""
    with open(filename, "r", encoding="UTF8") as f:
        for line in f:
            print(line)
