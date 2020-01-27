#!/usr/bin/python3
'''rectangle file'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle Class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Rectangle __init__'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width property'''
        return self.__width

    @property
    def height(self):
        '''height property'''
        return self.__height

    @property
    def x(self):
        '''x property'''
        return self.__x

    @property
    def y(self):
        '''y property'''
        return self.__y

    @width.setter
    def width(self, value):
        '''width Setter'''
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        '''height Setter'''
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @x.setter
    def x(self, value):
        '''x Setter'''
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @y.setter
    def y(self, value):
        '''y Setter'''
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")
