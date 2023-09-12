#!/usr/bin/python3
"""Task: 0.Read files"""


def read_file(filename=""):
    """function reads text file as UTF8 and prints it"""
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
        for i in lines:
            print(i)
