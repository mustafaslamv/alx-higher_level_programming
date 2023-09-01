"""task: 5. Printing a square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square. Default is 0.
        """
        self.__size = size

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

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        char = '#'
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print(char * self.size)
