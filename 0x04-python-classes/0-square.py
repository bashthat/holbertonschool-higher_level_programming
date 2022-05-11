#!/usr/bin/python3
"""The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. """

class Square:
    """ a simple Square that defines the private instance of size, and instantiation with size.
    """
    def __init__(self, size=0):
        """ utilizing type errors """
        
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
