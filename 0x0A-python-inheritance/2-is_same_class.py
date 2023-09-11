#!/usr/bin/python3
"""Task: 2. Exact same object"""


def is_same_class(obj, a_class):
    """Checks if the object is an exact instance of the class.
    
    Returns:
    
    True if the object is an exact instance of the class, False otherwise.

        Note: 5 is instance of int and object as int inherit from object
        but it is exact instance of int only
    """
    return type(obj) == a_class
