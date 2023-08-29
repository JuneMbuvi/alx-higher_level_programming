#!/usr/bin/python3
""" creating a class with three public instances"""


class Square:
    """initialize the private instance"""
    def __init__(self, size=0):
        self.__size = size

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

    """creating public instances"""
    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        for i in range(0, self.__size):
            [print("#", end="")for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
