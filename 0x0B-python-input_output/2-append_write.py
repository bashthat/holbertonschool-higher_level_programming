#!/usr/bin/python3
'''
utilizing the append and write os function
'''


def append_write(filename="", text=""):
    '''
    utilizing the with statement to open/write/append a file.txt
    '''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)  
