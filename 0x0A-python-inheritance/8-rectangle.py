#!/usr/bin/python3
""" defines a class Rectangle that inherits from BaseGeometry"""


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

        """creating a subclass Rectangle"""


class Rectangle(BaseGeometry):
    """the constructor method"""
    def __init__(self, width, height):
        """validating both width & height with integer_validator"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
