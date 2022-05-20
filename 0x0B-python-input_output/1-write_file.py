#!/usr/bin/python3
'''
writing into a file
'''

def write_file(filename="", text=""):

    with open(filename, "w", text) as file:
        return file.write(text)
        print(len(text))
