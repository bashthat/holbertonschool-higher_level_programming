#!/usr/bin/python3
"""the size of a square is crucial to the python in the box!"""


class Square:
    """a simple Square that defines the size
    """
def __init__(self, size=0):
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    def area(self):
        return(self.__area = area)
