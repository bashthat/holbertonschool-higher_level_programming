#!/usr/bin/python3
import json
'''
json import
returning a string
'''

def from_json_string(my_str):
    '''
    return my_str
    '''
    return json.load(my_str)
