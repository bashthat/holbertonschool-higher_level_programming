#!/usr/bin/python3
'''
BaseGeometry
'''


class BaseGeometry:
    '''
    class method Basegeometry
    '''
    pass

    def area(self):
        '''
        the area
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
            '''
            validates the value of int
            '''
        if type(value) != int:
            raise TypeError print("{} must be greater than 0".format(name))
            return False
        if value <= 0:
            raise ValueError print("{} must be greater than 0".format(name))
            return False
        else:
            return value
