#!/usr/bin/python3
'''
basic sytax to write into a README using python
'''

lines = ['Readme', 'How to write text files in Python']
with open('README.md', 'w') as file:
        file.writelines(lines)
