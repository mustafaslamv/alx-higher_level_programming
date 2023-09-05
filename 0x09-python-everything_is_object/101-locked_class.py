#!/usr/bin/python3
"""Task: 30. Low memory cost"""


class LockedClass(object):
    """class LockedClass with no class or object attribute"""

    __slots__ = ["first_name"]

    def __init__(self):
        pass
