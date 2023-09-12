#!/usr/bin/python3
"""defines a function for reading files"""


def read_file(filename=""):
    """we use the read() with the filename
    we don't have to pass a mode since its default is read"""
    with open('my_file_0.txt', encoding="UTF8") as filename:
        print(filename.read())
