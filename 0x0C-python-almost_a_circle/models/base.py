#!/usr/bin/python3
"""Task: 1. Base class"""
import json


class Base:
    """Base class for all the derived classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        result = []
        if list_objs is not None:
            for i in list_objs:
                result.append(i.to_dictionary())
        result = cls.to_json_string(result)
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            file.write(result)

    @staticmethod
    def from_json_string(json_string):
        result = []
        if json_string is None or json_string == "":
            return result
        else:
            result = json.loads(json_string)
        return result

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1, 1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1, 1, 1)
        instance.update(**dictionary)
        return instance
