#!/usr/bin/python3
def value(m):
    if (m == 'I'):
        return (1)
    if (m == 'V'):
        return (5)
    if (m == 'X'):
        return (10)
    if (m == 'L'):
        return (50)
    if (m == 'C'):
        return (100)
    if (m == 'D'):
        return (500)
    if (m == 'M'):
        return (1000)
    return (-1)


def roman_to_int(roman_string):
    res = 0
    i = 0

    while (i < len(roman_string)):
        s1 = value(roman_string[i])
        if (i + 1 < len(roman_string)):
            s2 = value(roman_string[i + 1])
            if s1 >= s2:
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return (res)
