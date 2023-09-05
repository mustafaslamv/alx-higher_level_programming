#!/usr/bin/python3
"""Task: 1. Divide a matrix"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(n, (int, float)) for r in matrix for n in r)):
        err_msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err_msg)

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    div_list = list(
        map(
            lambda row: list(map(lambda num: round(num / div, 2), row)), matrix
        )
    )
    return div_list
