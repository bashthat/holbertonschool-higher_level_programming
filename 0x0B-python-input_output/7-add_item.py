#!/usr/bin/python3
'''importing the operation calls for importing args to json file '''
import sys
import json
import os
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file
'''
utilizing the sys for writing into a file
'''
file = []
'''add item.json for function
'''
try:
    file = load_from_json_file(file + sys.argv[1:], "add_item.json")
except:
    save_to_json_file(file + sys.argv[1:], "add_item.json")
'''
saturday will be the day
'''
