#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
