#!/usr/bin/python3
"""defines module for creating a geometry class"""


class BaseGeometry:
    """start with the constructor"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
