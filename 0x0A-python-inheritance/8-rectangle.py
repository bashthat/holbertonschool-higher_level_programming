#!/usr/bin/python3
'''theClass BaseG'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    define the rectangle
    '''
    def __init__(self, width, height):
        '''
        the width and height
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
