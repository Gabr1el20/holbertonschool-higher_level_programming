#!/usr/bin/python3
"Task 1"


def matrix_divided(matrix, div):
    "Divides a matrix elements by div"
    errore = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    lengi = len(matrix[0])
    dividedMat = []
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(errore)
    for row in matrix:
        dividedrow = []
        for each in row:
            dividedElem = round(each / div, 2)
            dividedrow.append(dividedElem)
        dividedMat.append(dividedrow)
    if len(row) != lengi:
        raise TypeError("Each row of the matrix must have the same size")
    return dividedMat
