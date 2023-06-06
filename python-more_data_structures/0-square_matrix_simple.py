#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    "A function that computes the square values of all int of a matrix"
    SquareMatrix = []
    for row in matrix:
        squareRow = []
        for element in row:
            squaredElement = element ** 2
            squareRow.append(squaredElement)
        SquareMatrix.append(squareRow)
    return SquareMatrix
