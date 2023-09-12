#!/usr/bin/python3
"""defines a function for deserializing"""
import json


def from_json_string(my_str):
    """using the load() to deserialize
    Args
    my_str - string being desrialized"""
    return (json.loads(my_str))
