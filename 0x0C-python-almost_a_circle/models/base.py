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

    """define a class method that writes the json of list_objs
    to a file"""
    @classmethod
    def save_to_file(cls, list_objs):
        """"returns the json repreentation of list_objs
        Args
        list_objs - list of instances who inherits of Base
        cls - class decorator"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                my_list = [m.to_dictionary for m in list_objs]
                jsonfile.write(Base.to_json_string(my_list))

    """define static method that returns list of JSON representation
    of json_string"""
    @staticmethod
    def from_json_string(json_string):
        """returns list of json representation
        Args
        json_string - string representing a list of dictionaries"""
        if json_string is None or json_string == '[]':
            return ([])
        return (json.loads(json_string))
