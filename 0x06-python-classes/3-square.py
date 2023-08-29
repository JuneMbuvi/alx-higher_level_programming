#!/usr/bin/python3
"""creating a class with both a private and public instance"""


class Square:
    """first create the attributes then private and public ones"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """creating a public instance"""
        return (self.__size * self.__size)
