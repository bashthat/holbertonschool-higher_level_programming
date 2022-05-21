#!/usr/bin/python3
'''
writing into a file
'''


def write_file(filename="", text=""):
    '''
    open then write to text in the return
    '''
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
