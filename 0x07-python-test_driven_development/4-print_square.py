#!/usr/bin/python3
'''
printinng a square as part of the function for the benefit of testing the code
'''

def print_square(size):
    if type(size) != int or type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    
    if size == 0:
        None

    if size < 0:
        raise ValueError("size must be >= 0")
    

    for xyz in range(size):
        for lemon in range(size):
            print("#", end='')
        print()