#!/usr/bin/python3
"""task: 5. Printing a square"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): tuple of 2 positive integers
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints in stdout the square with the character #.
        """
        if self.size == 0:
            print("")
        else:
            for _ in range(self.position[1]):
                print("")
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
