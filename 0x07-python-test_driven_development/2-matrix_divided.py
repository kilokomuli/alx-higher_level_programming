#!/usr/bin/python3
"""Defines function matrix_divided which divides all elements of
a matrix
Attributes:
    matrix and div"""


def matrix_divided(matrix, div):
    """Divodes all elements of a matrix
    Args:
        matrix: list of lists of integers or floats
        div: number inter or a float
    Raises:
        TypeError: when matrix is not list of lists of integers or each
        row is not of the same size
        TypeError: if div is not a number int or float
        ZeroDivisionError: if div is equal to zero
    Return:
        new matrix"""
    row_size = None
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(message)

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(message)

        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(message)

        if row_size is None:
            row_size = len(i)
        elif row_size != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return new_matrix
