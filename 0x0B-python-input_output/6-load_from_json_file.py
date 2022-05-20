#!/usr/bin/python3
import json
'''
the json sys operation
'''


def load_from_json_file(filename):
    '''
    creating the JSON file
    '''
    with open(filename, "w", encoding="utf-8") as filez:
        '''
        open then write to filez to return the content.
        '''
        return json.load(filez)
