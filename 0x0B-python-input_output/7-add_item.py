#!/usr/bin/python3
'''importing the operation calls for importing args to json file '''
import sys
import os.path
import json
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file
'''
utilizing the sys for writing into a file
'''
file = "add_item.json"
json_list = []
if os.path.exists(file):
    json_list = load_from_json_file(file)

for xyz in range(1, len(sys.argv)):
    json_list.append(sys.argv[xyz])

    save_to_json_file(json_list, file)
