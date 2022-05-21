#!/usr/bin/python3
'''
simple system call to open and read a file
'''


def read_file(filename=""):
    '''
    read file, with!
    '''
    with open(filename, encoding="utf-8") as f:
        '''
        print
        '''
        print(f.read(), end="")
