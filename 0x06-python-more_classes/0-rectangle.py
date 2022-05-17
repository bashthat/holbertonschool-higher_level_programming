#!/usr/bin/python3
''' this is a class initializing a Rectangle'''


class Rectangle:
    '''the dimensions of the triangle being defined through attributes'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
            return (self.__width)

    @width.setter
    def width(self, value):
        '''setting the width of the rectangle'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        '''setting the height of the equation'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
        