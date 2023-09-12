#!/usr/bin/python3
"""defines a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """open the file with the open() then use the load()
    to deserialize"""
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
