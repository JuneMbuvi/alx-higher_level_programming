#!/usr/bin/python3
"""defines a class Square that inherits from Rectangle
so we import the relevant module"""

Rectangle = __import__('9-rectangle').Rectangle


"""creating a subclass Square that inherits from Rectangle"""


class Square(Rectangle):
    """start with th constructor method"""
    def __init__(self, size):
        """to validate size with integer_validator"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """define the str() to print the string representation of square"""
    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return (string)
