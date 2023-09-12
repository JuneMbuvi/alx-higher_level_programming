#!/usr/bin/python3
"""defines a function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """we start by opening the file with open then
    we serialize using dump().
    Args
    my_obj - object being written to text file
    filename - name of file"""
    with open(filename, "w", encoding="utf-8") as f:
        return (json.dump(my_obj, f))
