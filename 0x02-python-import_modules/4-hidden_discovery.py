#!/usr/bin/python3
# type: ignore
import hidden_4

if __name__ == "__main__":

    list = dir(hidden_4)

    for func in list:
        if func[:2] != "__":
            print("{:s}".format(func))
