#!/usr/bin/python3
"""Task: 1. My list"""
import doctest


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """I really do not understand how this works"""
        print(sorted(self))
