#!/usr/bin/python3
"""creates a class Base"""


class Base:
    """create class attribute(s)"""
    __nb_objects = 0
    """constructor method"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
