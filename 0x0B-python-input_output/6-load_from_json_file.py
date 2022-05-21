#!/usr/bin/python3
import json
'''
the json sys operation
'''


def load_from_json_file(filename):
    '''
    creating the JSON file
    '''
    with open(filename, mode="r", encoding="utf-8") as fig:
        '''
        open then write to filez to return the content.
        '''
        return json.load(fig)
