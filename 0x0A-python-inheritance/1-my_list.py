#!/usr/bin/python3
"""Task: 1. My list"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        print(list(sorted(self)))
