#!/usr/bin/python3
'''this is a prototype that returns an integer or float as part of a function '''


def add_integer(a, b=98):
    if type(a) == float:
        a = int
    elif type(a) != int:
        raise TypeError ("a must be an integer")

    if type(b) == float:
        b = int
    elif type(a) != int:
        raise TypeError("b must be an integer")
    '''adding both integers as a return'''
    return int(a) + int(b)