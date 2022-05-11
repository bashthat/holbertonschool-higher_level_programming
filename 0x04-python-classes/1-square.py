#!/usr/bin/python3
"""The size of a square is crucial, control the type and value of this attribute. """
class Square:
    

    """ a simple Square that defines the private instance of size.
    
    
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
