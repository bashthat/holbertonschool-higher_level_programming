#!/usr/bin/python3
''' this is a class initializing a Rectangle'''


class Rectangle:
    '''the dimensions of the triangle being described in a function'''
    def __init__(self, width=0, height=0):
    
    @property
        def width(self):
            self.width = width
    
    @width.setter
        def width(self):    
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >= 0")
            self.width = width
            
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >= 0")
            self.width = width