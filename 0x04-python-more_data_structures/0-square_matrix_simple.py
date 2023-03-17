#!/usr/bin/python3
def square_matrix_simple(matrix=None):
    if matrix is None:
        matrix = []
    return [list(map(lambda n: n**2, i)) for i in matrix]

