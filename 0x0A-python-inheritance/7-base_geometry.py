#!/usr/bin/python3
"""Task: 7. Integer validator"""


class BaseGeometry:
    """BaseGeometry class contains some methods"""

    def area(self):
        """area() is not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validated 'value' int or not, more than 0 or not"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
