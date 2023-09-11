#!/usr/bin/python3
"""Task: 4. Only sub class of"""


def inherits_from(obj, a_class):
    """function returns True if the object is an instance otherwise False"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
