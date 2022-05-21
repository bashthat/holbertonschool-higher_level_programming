#!/usr/bin/python3
'''
class to json import
'''

def class_to_json(obj):
    '''return dictionary description'''
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
