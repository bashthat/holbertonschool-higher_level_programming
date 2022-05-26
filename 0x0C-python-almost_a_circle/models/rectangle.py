#!/usr/bin/python3
'''rectangle'''


from models.base import Base


class Rectangle:
    '''the class Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' assigning attributes correctly for definition
            given the super() function and handling the arguments
            to the Rectangles peramaters
            ===========================
            *initializing the rectangle*
            '''

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    '''the getters for the initialized rectangle'''
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

        '''defining the area
    hence the getter property '''

    @property
    def area(self):
        '''area of the rectangle'''
        return (self.__width * self.__height)

    def display(self):
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for z in range(self.__height)))

    def __str__(self):
        '''the return'''
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''updates multiple arguments'''
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
