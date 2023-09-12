#!/usr/bin/python3
"""defines a student class"""


class Student:
    """constructor method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """public method for retrieving dictionary representation of Student"""
    def to_json(self):
        """the dict() is used to get dictionary representations"""
        return (self.__dict__)
