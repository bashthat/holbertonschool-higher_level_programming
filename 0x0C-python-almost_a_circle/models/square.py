#!/usr/bin/python3
"""
the inherent square of the rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherent to the rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        init for the sake of a super function
        """
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """
        Returning the squares dictionary
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """
        updating attributes with new arguments
        """
        if not args:
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
            attrs, i = ['id', 'size', 'x', 'y'], 0
            for value in args:
                setattr(self, attrs[i], value)
                i += 1

    def __str__(self):
        """
        string cheese in the shape of a square
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}\
 - {self.width}"

    @property
    def size(self):
        """
        getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter
        """
        self.width = self.hw_validator("width", value)
        self.height = self.hw_validator("width", value)
