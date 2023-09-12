#!/usr/bin/python3
"""defines a function that adds all arguments to a Python list,
and then save them to a file"""
import sys
import os
import json


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =\
            __import__('6-load_from_json_file').load_from_json_file

"""check whether the file exists and if not create one"""
if os.path.exists("add_item.json"):
    py_list = load_from_json_file("add_item.json")
else:
    py_list = []

"""add cmdline args to the list"""
for arg in sys.argv[1:]:
    py_list.append(arg)

save_to_json_file(py_list, "add_item.json")
