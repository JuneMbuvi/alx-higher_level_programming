#!/usr/bin/python3
"""defines a module for testing the isinstance method"""


def is_kind_of_class(obj, a_class):
    """to test for instances in classes, the isinstance() is used"""
    if isinstance(obj, a_class):
        return True
    return False
