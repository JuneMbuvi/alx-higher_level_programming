#!/usr/bin/python3
"""creating a square class"""


class Square:
    def __init__(self, size=0):
        """initializing the Square"""
        self.__size = size
        """using the getter to access the size property"""
    @property
    def size(self):
        return (self.__size)
    """using the setter to update the class instances"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """creating the public instance area"""
    def area(self):
        return (self.__size * self.__size)
