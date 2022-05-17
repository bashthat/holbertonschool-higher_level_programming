#!/usr/bin/python3
'''this is a prototype that returns an integer'''


def add_integer(a, b=98):
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
        a = int(a)
        b = int(b)
    '''adding both integers as a return'''
    return a + b
