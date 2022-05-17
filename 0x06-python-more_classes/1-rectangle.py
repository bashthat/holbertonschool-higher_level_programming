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
        def perimeter(self):
            return ((self.__width * 2) + (self.__height * 2))
        
        @property
        def width(self):
            return (self.__width)

        @property
        def height(self):        
            return(self.__height)
        
        @width.setter
        def width(self, value):
            '''setting the width of the rectangle'''        
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            if width < 0:
                raise ValueError('width must be >= 0')
            self.__width = value
            return("\n")
        
        @height.setter
        def height(self, value):
            '''setting the height of the equation'''
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            if height < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
            return("\n")
