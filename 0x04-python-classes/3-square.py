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
    self.__size = size
    
    def area(self):
        """ returns the area """
        return (self.__size ** 2)

    @size.setter
    def size(self, value):
        """setter for the size of the square input"""
    if type(size) != int:
       	raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size


    @property
    def size(self):
        return self.__size

    @size.getter
    def size(self):
        """size setter and getter with errors"""


    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size 