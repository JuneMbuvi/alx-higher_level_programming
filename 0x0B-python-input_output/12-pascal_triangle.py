#!/usr/bin/python3
"""defines a function that returns a list of lists of
integers representing the Pascal’s triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle"""
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return (triangles)
