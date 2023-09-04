#!/usr/bin/python3
"""Task: 8. Compare rectangles"""


class Rectangle:
    """Empty class Rectangle that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            result += (str(self.print_symbol) * self.width)
            if i != self.height-1:
                result += "\n"
        return result

    def __repr__(self):
        """formal string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """destructor called when an instance of Rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 >= area2:
            return rect_1
        else:
            return rect_2
