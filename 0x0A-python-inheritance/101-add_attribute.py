#!/usr/bin/python3
"""Task: 13. Can I?"""


def add_attribute(instance, name, value):
    """function that adds a new attribute to an object if it’s possible"""

    if not hasattr(instance, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(instance, name, value)
