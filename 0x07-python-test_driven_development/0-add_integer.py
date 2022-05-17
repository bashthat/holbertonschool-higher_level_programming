#!/usr/bin/python3
'''this is a prototype that returns an integer'''


def add_integer(a, b=98):
    if isinstance(a, float):
        a = int
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")

    if isinstance(b, float):
        b = int

    elif not isinstance(a, int):
        raise TypeError("b must be an integer")
    '''adding both integers as a return'''
    return int(a) + int(b)
