#!/usr/bin/python3
''' this is a class initializing a Rectangle'''


class Rectangle:
    '''the dimensions of the triangle being defined in through attributes'''
    def __init__(self, width=0, height=0):
        
        def width(self):
            self.__width = width
            self.__height = height
        
        @property
        def area(self):
            return self.__width * self.__height 
        
        @setter.width
        
        def width(self): 
        
            if type(width) != int:
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be >= 0")
        
        def height(self):
            
            if type(height) != int:
                raise TypeError("width must be an integer")
            if height <= 0:
                raise ValueError("width must be >= 0")
            self.height = height