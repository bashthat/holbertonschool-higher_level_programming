#!/usr/bin/python3
'''rectangle'''

class Rectangle

    '''this is the fun program where we design a series of functions
    which in turn work together in the python unittesting module
    and classes to print a rectangle'''

    
    def __init__(self, width, height, x=0, y=0, id=None):
    
    ''' assigning attributes correctly for def
        given the known method to handling the arguments'''
    
    self.__width = width
    self.__height = height
    self.__x = x
    self.__y = y
    
    super().__init__()
    
    TypeError('<name of the attribute> must be an integer')
    ValueError('<name of the attribute> must be > 0')
    ValueError('<name of the attribute> must be >= 0')

    '''defining the area
    hence the getter property '''
    
    @property
        def area(self):
            return (self.__width * self.__height)
    
    

    def display(self):

    def __str__(self):
    '''the return'''
    return ([Rectangle] (<id>) <x>/<y> - <width>/<height>)
