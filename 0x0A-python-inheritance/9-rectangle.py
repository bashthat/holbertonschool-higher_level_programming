#!/usr/bin/python3
'''the class basegeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    the rectangle
    '''
    def __init__(self, width, height):
        '''
        defiiniing the rectangle
        '''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
    def area(self):
        '''
        the area
        '''
        return self.__width * self.__height
    def __str__(self):
        '''
        strings
        '''
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
