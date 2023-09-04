#!/usr/bin/python3
"""Task: 4. Eval is magic"""


class Rectangle:
    """Empty class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Rectangle area instance method"""
        return (self.width * self.height)

    def perimeter(self):
        """Rectangle perimeter instance method"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """return class instance as a Rectangle W * H made of '#'"""
        result = ""
        if self.height == 0 or self.width == 0:
            return result
        for i in range(self.height):
            result += ("#" * self.width)
            if i != self.height-1:
                result += "\n"
        return result

    def __repr__(self):
        """formal string representation of the rectangle"""
        return f"Rectangle({self.width},{self.height})"
