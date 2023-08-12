#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for ROWitems in matrix:
        last_index = len(ROWitems) - 1
        for i, COLitems in enumerate(ROWitems):
            print("{:d}".format(COLitems), end="")
            if i != last_index:
                print(" ", end="")
        print("")
