#!/usr/bin/python3


def print_square(size):
    """prints a square with the # symbol.
    size is the size length of the square."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        [print('#', end="")for j in range(size)]
        print("")
