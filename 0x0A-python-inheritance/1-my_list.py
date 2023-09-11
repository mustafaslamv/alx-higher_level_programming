#!/usr/bin/python3
"""Task: 1. My list"""


class MyList(list):
    """class MyList that inherits from list"""

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    def print_sorted(self):
        print(sorted(self))
