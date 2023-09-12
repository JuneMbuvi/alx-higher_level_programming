#!/usr/bin/python3
"""defines a rectangle that inherits from BaseGeometry with
several instances"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""defining a subclass Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """the constructor method"""
    def __init__(self, width, height):
        """validating both width & height with integer_validator"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """define a method area"""
    def area(self):
        return (self.__width * self.__height)

    """defining str() to print the string representation of the rectanle"""
    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return (string)
