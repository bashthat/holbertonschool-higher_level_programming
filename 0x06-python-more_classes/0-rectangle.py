#!/usr/bin/python3
    ''' this is a class initializing a Rectangle'''


class Rectangle:
    '''the dimensions of the triangle being defined in through attributes'''
    def __init__(self, width=0, height=0):
        
        def width(self):
            self.__width = width
            self.__height = height
    ''' the definition of the objects IO '''     
        @property
        def width(self):
            return (self.__width)
        
        @width.setter
            def width(self, value)        
            
            if type(self) != int:
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be >= 0")
        
        @property
            def height(self):
                return (self.__height)    
        
        def height(self, value):
            
            if type(self) != int:
                raise TypeError("height must be an integer")
            if height <= 0:
                raise ValueError("height must be >= 0")
            self.__height = height