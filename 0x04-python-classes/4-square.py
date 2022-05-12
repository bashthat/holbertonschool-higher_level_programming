#!/usr/bin/python3
"""the size of a square is crucial"""


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

        """the area is defined!"""
	
        def area(self):
		"""Finds the area of a square
		Returns:
			int: the squares area
		"""
		return self.__size ** 2

            """need to return the size, no over-achieving!"""
            @property
            """returns the size of the square"""
            def size(self):
                return self.__size

            """set the size of the square with the call of size setter"""
            @size.setter
            def size(self, value)
                if type(value) != int:
                    raise TypeError("size must be an integer")
                if value < 0:
                    raise ValueError("size must be >= 0")
                self.__size = value
