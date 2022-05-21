#!/usr/bin/python3

'''
simple system call to open and read a file
'''

def read_file(filename=""):
    '''
    read file, with!
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        '''
        defining the text
        '''
        text = f.read()
        print(f.read(), end="")
