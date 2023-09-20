#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class derived from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area method"""
        return self.width * self.height

    def display(self):
        """ prints the Rectangle instance with the character #"""
        result = ""
        for i in range(self.height):
            result += (self.x * " " + "#" * self.width)
            if i != self.height - 1:
                result += "\n"
        result = "\n" * self.y + result
        print(result)

    def __str__(self) -> str:
        return f"[Rectangle] ({self.id}) {self.x}/\
{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        result = {
            "id" : self.id,
            "width" : self.width,
            "height" : self.height,
            "x" : self.x,
            "y" : self.y
        }
        return result
