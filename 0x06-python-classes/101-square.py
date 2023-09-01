#!/usr/bin/python3
"""task: 8. Print Square instance"""


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

    def __str__(self):
        """
        Return a string representation of the square with the character '#'
        """
        printed_square = ""
        if self.__size == 0:
            return printed_square

        for _ in range(self.__position[1]):
            printed_square += "\n"
        for _ in range(self.__size):
            printed_square += (" " * self.__position[0] +
                               "#" * self.__size +
                               '\n')

        return printed_square.rstrip('\n')
