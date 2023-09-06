#!/usr/bin/python3
"""creating a class Rectangle"""


class Rectangle:
    """first we create the attributes of the rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """use getters and setters to retrieve & access the width"""
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """use getters and setters to retrieve & access the height"""
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """defining public instance area"""
    def area(self):
        return (self.__width * self.__height)

    """defining public instance, perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return (2 * (self.__width + self.__height))
