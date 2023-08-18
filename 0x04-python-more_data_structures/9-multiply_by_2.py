#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    Keys = list(new.keys())
    for i in Keys:
        new[i] *= 2
    return (new)
