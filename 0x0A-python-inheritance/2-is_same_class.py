#!/usr/bin/python3
"""defines a module for testing instances of classes"""


def is_same_class(obj, a_class):
    """to test exact instances of a class, the type() is used"""
    return (type(obj) is a_class)
