#!/usr/bin/python3
"""creating a square class"""


class Square:
    """creating the private instance of the square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """creating a public instance"""
    def area(self):
        return (self.__size * self.__size)
