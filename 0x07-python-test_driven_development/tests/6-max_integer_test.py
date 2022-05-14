#!/usr/bin/python3
'''
our test file should be inside a folder tests
You have to use the unittest module
Your test file should be python files (extension: .py)
Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
All tests you make must be passable by the function below
We strongly encourage you to work together on test cases, so that you don’t miss any edge case01~
'''

from re import X


def max_integer(list=[]):
    '''a function wich returns none if the list is empty
    
    it is a curious one, max_integer
    '''

    if len(list) == 0:
        return None
    
    
    result = list[0]
    xyz = 1
    
    '''function where the result is a list hence, None if empty'''

    while xyz < len(list):
        if list[xyz] > result:
            result = list[xyz]
        xyz += 1
    
    '''returning the result of the function'''
    
    return result




