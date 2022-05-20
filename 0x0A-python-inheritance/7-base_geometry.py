#!/usr/bin/python3
'''the BaseGeometry Class'''


class BaseGeometry:
    '''
    area defined
    '''
    def area(self):
        '''Exception message'''
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        '''
        type and value errors
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
