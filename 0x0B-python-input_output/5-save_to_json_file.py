#!/usr/bin/python3
import json
'''
using json to write to a file.txt
'''


def save_to_json_file(my_obj, filename):
    '''
    using the open function to utilize write
    as part of the json.dump function in the
    returned value of the args in the function
    '''
    with open(filename, "w", encoding="utf-8") as fig:
        return json.dump(my_obj, fig)
