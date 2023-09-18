#!/usr/bin/python3
from models.rectangle import Rectangle
"""defines a class Square that inherits from Rectangle"""


class Square(Rectangle):
    """constructor method"""
    def __init__(self, size, x=0, y=0, id=None):
        """inherit attributes from the super or Rectangle class"""
        super().__init__(size, size, x, y, id)

    """define the square's string representation"""
    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y)
        string += " - " + str(self.width)
        return (string)
