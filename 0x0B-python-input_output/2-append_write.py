#!/usr/bin/python3
'''
utilizing the append and write os function
'''


def append_write(filename="", text=""):
    '''
    utilizing the with statement to open/write/append a file.txt
    '''
    with open(filename, "r", text) as f:
        text = f.read()
        return len(text)  
