#!/usr/bin/python3
"""defines a function that adds a new attribute
to an object if it’s possible"""


def add_attribute(obj, name, value):
    """check if it is possible to add attributes
    using the hasattr()"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
