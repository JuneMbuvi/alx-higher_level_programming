#!/usr/bin/python3
"""defines a module for testing the issubclass function"""


def inherits_from(obj, a_class):
    """to test for direct/indirect subclassess"""
    return (isinstance(obj, a_class) and not obj.__class__ == a_class)
