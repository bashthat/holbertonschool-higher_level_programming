#!/usr/bin/python3
"""the size of a square is crucial"""


class Square:
	""" a simple Square that defines the private instance of size.
            the size and area are being swapped hence the statement
	"""
	def __init__(self, size=0):
		self.__size = size
        

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
