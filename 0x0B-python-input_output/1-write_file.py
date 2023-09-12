#!/usr/bin/python3
"""defines a function that writes a string to a text file
(UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """implementing the write() to print a string and
    the total number of chars it prints.

    Args
    filename - name of file
    text - string being input"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
