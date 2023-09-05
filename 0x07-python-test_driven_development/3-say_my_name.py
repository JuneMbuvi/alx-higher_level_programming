#!/usr/bin/python3
"""defines a function that prints a persons name.
It takes both a first name and a second name.
If a non-sring is passed, a TypeError is raised."""


def say_my_name(first_name, last_name=""):
    if not (isinstance(first_name, str)):
        raise  TypeError("first_name must be a string")
    if not(isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
