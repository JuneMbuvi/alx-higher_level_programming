#!/usr/bin/python3
"""defines a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers
    list_of_integers - numbers/unsorted array
    Return - int"""
    mylist = list_of_integers
    """if empty return None"""
    if mylist == []:
        return None
    length = len(mylist)
    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if mylist[mid] > mylist[mid - 1] and mylist[mid] > mylist[mid + 1]:
            return mylist[mid]
        if mylist[mid - 1] > mylist[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return mylist[start]
