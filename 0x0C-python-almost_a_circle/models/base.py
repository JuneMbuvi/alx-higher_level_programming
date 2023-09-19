#!/usr/bin/python3
"""creates a class Base"""
import json


class Base:
    """create class attribute(s) that increments everytime
    an oobject is created"""
    __nb_objects = 0
    """constructor method"""
    def __init__(self, id=None):
        """initializez the Base class with an id and returns id if found.
        Args
        id - returns id of the object created"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """define static method & return JSON representation of
    list_dictionaries"""
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the string representation of list_dictionaries
        if list is empty return empty list "[]".
        Args
        list_dictionaries - is a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return (json.dumps(list_dictionaries))
