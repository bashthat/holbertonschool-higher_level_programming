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
