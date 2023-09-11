#!/usr/bin/python3
"""creating a function that returns list of available attributes & methods.
The function should return a list object"""


def lookup(obj):
    """the dir() returns all properties & methods of an object"""
    return (dir(obj))
