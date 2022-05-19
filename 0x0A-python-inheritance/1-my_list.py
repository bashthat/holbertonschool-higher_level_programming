#!/usr/bin/python3
'''prints sorted list'''


class MyList(list):
    def print_sorted(self):
        return print(sorted(self))
