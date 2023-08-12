#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ROWitems in matrix:
        for Citems in ROWitems:
            print("{:d}".format(Citems), end=" ")
        print("")
