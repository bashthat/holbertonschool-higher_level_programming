#!/usr/bin/python3
"""the size of a square is crucial"""


class Square:
	""" a simple Square that defines the private instance of size.
	"""
	def __init__(self, size=0):
		if type(size) != int:
			raise TypeError("size must be an integer")
		if size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size

	def area(self):
		"""Finds the area of a square
		Returns:
			int: the squares area
		"""
		return self.__size ** 2

            """need to return the size, no over-achieving!"""
            @property
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
