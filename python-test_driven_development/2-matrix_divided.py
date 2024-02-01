#!/usr/bin/python3
'''
Testing excercises
'''
def matrix_divided(matrix, div):
    '''
    Function to return a new matrix
    '''
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    count = len(matrix[0])
    for i in matrix:
        if count != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = []  # Initialize as an empty list, not [[]]
    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)

    return new_matrix
