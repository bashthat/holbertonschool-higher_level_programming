#!/usr/bin/python3
import os
'''
importing the operating system
'''

def read_file(filename=""):
    '''
    read file, with!
    '''
    with open(filename, 'r') as f:
        print(f.read(), end="")
