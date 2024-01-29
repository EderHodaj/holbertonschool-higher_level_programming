#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_lists = []
        for element in row:
            new_lists.append(element ** 2)
        new_matrix.append(new_lists)
    return new_matrix
