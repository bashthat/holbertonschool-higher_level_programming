#!/usr/bin/python3
'''
prints sorted list
'''


class MyList(list):
    '''
    The Class of the list
    '''
    def print_sorted(self):
        print(sorted(self))
