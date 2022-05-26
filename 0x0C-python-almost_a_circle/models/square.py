#!/usr/bin/python3
'''
class Square(Rectangle)
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    utilizing super() for the Square(Rectangle) philosophy
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        __init__ defines the initialization of the square as a function
        while the super class logic is applied to the square class attributes
        from the Rectangle Class'''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        if len(args):
            for z, a in enumerate(args):
                if z == 0:
                    self.id = a
                elif z == 1:
                    self.size = a
                elif z == 2:
                    self.x = a
                elif z == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
