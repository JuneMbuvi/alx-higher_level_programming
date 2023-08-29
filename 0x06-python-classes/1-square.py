#!/usr/bin/python3
"""introducing the concept of encapsulation"""


class Square:
    """creating a private instance of the class"""
    def __init__(self, size=0):
        self.__size = size
