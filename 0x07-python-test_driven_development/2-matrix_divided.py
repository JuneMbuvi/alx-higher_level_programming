#!/usr/bin/python3
#2-matrix_divided.py
"""defines a function for dividing a matrix"""
def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
