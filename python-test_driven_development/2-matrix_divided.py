#!/usr/bin/python3
"""
Divide a matrix
"""


def matrix_divided(matrix, div):
    """
        Parameters:
        matrix (int, float): matrix.
        div (int, float): the divisor of the matrix.

        Returns:
        float: The quotient of the matrix.

        Example:
        add(2, 3)
        5
    """

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    row_len = len(matrix[0])
    new_matrix = []
    for row in matrix:
        new_row = []
        if len(row) != row_len:
            raise TypeError('Each row of the matrix must have the same size')
        for elem in row:
            if type(elem) not in [int, float]:
                raise_err()
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)
    return new_matrix

def raise_err():
    a = 'matrix must be a matrix (list of lists) of integers/floats'
    raise TypeError(a)
