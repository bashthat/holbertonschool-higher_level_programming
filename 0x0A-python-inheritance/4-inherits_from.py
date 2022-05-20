#!/usr/bin/python3
'''obj and class'''


def inherits_from(obj, a_class):
    '''returns True if the object is an instance of a class'''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
