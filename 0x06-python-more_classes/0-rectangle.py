#!/usr/bin/python3
''' this is a class initializing a Rectangle'''


class Rectangle:
    '''the dimensions of the triangle being defined through attributes'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
        @property
        def area(self):
            return self.__width * self.__height
        
        @property
        def width(self):
            return (self.__width)

        @property
        def height(self):        
            return(self.__height)
        
        @width.setter
        def width(self, value):
            self.__width = value        
            if not isinstance(self, int):
                raise TypeError('width must be an integer')
            if width < 0:
                raise ValueError('width must be >= 0')
            return("\n")
        
        @height.setter
        def height(self, value):
            self.__height = value
            if not isinstance(self, int):
                raise TypeError('height must be an integer')
            if height < 0:
                raise ValueError('height must be >= 0')
            return("\n")