#!/usr/bin/python3
"""defines module for creating a geometry class"""


class BaseGeometry:
    """start with the constructor"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    """defining a public instance to validate a value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
