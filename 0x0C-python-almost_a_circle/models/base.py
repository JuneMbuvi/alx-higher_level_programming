#!/usr/bin/python3
import json
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

    """define static method & return JSON representation of
    list_dictionaries"""
    @staticmethod
    def to_json_string(list_dictionaries):
        """if list is empty return empty list"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return (json.dumps(list_dictionaries))
