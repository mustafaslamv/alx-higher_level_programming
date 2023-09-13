#!/usr/bin/python3
"""Task: student class to JSON"""


class Student:
    """simple student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            dict = self.__dict__
            result = {}
            for i in attrs:
                if i in dict:
                    result[i] = dict.get(i)
        else:
            result = self.__dict__
        return result
