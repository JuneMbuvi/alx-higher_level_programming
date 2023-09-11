#!/usr/bin/python3
"""module that shows an example of inheritance"""


class MyList(list):
    """start with the constructor method"""
    def __init__(self):
        pass

    """create method for sorting list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        for item in sorted_list:
            print(item, end="")
