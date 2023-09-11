#!/usr/bin/python3
"""Task: 10. Square #1"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
