#!/usr/bin/python3
'''
writing into a file
'''

def write_file(filename="", text=""):

    with open(filename, "w", text) as f:
        return f.write(text)
        print(len(text))
