#!/usr/bin/python3
"the size of a square is crucial"


class Square:
	" a simple Square that defines the private instance of size."
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
	
        def my_print(self):
            if self.size > 0:
                for i in range(self.__size):
                    for j in range(self.__size):
                        print("#", end="")
                    print()
            else:
                print()

        def area(self):
            return(self.__size ** 2)

        @property
        def size(self):
            return(self.__size)

        @size.setter
        def size(self, value)
            if type(value) != int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
