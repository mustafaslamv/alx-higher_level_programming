#!/usr/bin/python3

from models.rectangle import Rectangle
from models.square import Square
if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    Rectangle(1,1)
    Square(1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
