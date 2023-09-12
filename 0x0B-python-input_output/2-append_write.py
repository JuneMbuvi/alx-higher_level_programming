#!usr/bin/python3
"""defines a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """appends text to end of file and creates file if none exists.
    Args
    filename - name of file
    text - string being input"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
