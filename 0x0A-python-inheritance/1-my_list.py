#!/usr/bin/python3
"""Task: 1. My list"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        print(sorted(self))
