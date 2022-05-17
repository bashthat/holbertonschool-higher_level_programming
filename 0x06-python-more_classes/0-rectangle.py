#!/usr/bin/python3
''' this is a class initializing a Rectangle'''


class Rectangle:
    '''the dimensions of the triangle being defined through attributes'''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        
        @property
        def width(self):
            return (self.__width)

        @property
        def height(self):        
            return(self.__height)
        
        @width.setter
        def width(self, value):
            self.__width = width        
            if type(self) is not int:
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
        
        @height.setter
        def height(self, value):
            self.__height = height
            if type(self) is not int:
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            return("\n")