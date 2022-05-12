#!/usr/bin/python3
    #size of a square is crucial


class Square:
    # a simple Square that defines the private instance of size.
    def __init__(self, size=0):
        '''initializes the size of the square.'''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
	
        def my_print(self):
    #prints a square with the character.
            if self.size > 0:
                for i in range(self.__size):
                    for j in range(self.__size):
                        print("#", end="")
                    print()
            else:
                print()

        def area(self):
    #returns the area of the square.
            return(self.__size ** 2)

        @property
    #returns the size of the square.
        def size(self):
            return(self.__size)

        @size.setter
    #sets the size of the square.
        def size(self, value):
            if type(value) != int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
