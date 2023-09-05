#!/usr/bin/python3
def add_integer(a, b=98):
    """returns the addition of a and b
    floats are casted into integers before addition
    a TypeError is raised if a and b are neither floats/integers"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
