#!/usr/bin/python3
'''squares are curcial in this project #'''


class Square:



   """ a simple Square that defines the private instance of size.
        the size and area are being swapped hence the statement
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """print the actual square"""

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
                print()
            else
               print()

   '''this class prints a square'''

    def __init__(self, size=0):
        self.size = size


   def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print()

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
