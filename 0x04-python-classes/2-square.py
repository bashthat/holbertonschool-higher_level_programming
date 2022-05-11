#!/usr/bin/python3
"""size of a square is crucial to the python in the box!"""


class Square(object):

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
        """
        tips given on proper syntax
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        """
        takking out all the rubbish to see what happens in the spaces between
        """
        def area(self):
            """finds the area of the square
                Returns:
                    int : The area of the square.
                """
            return(self.__size * self.__size)
