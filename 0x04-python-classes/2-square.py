#!/usr/bin/python3
"""the size of a square is crucial to the python in the box!"""



class Square:
    """a simple Square defines the size naturally
    
    Attributes:
    __size (int): size of the square.
    Return:
        int : self.__size ** 2
    Raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0

    """
    
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """area of the squre"""

            return self.__size ** 2

        @property
        def size(self):


            return self.__size


        @size.setter

        def size(self, value):
            if type(value) != int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
