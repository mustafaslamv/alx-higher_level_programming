#!/usr/bin/python3
"""Task: 1. My list"""
import doctest

class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))

if __name__ == "__main__":
    doctest.testfile("tests/1-my_list.txt")
