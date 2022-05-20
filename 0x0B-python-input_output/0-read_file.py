#!/usr/bin/python3
import os
'''
importing the operating system
'''

def read_file(filename=""):
    '''
    read file, with!
    '''
    with open(filename, 'r', encoding="utf") as f:
        '''
        defining the text
        '''
        text = f.read()
        print(f.read(), end="")
