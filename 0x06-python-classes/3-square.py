#!/usr/bin/python3
"""creating a class with both a private and public instance"""


class Square:
    """first create the attributes then private instance and lastly the public one"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    """creating public instance"""
    def area(self):
        return (self.__size * self.__size)
