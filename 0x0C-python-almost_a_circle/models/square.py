#!/usr/bin/python3
""" square file """
from models.rectangle import Rectangle


class Square(Rectangle):
    '''square Class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''___init___ function'''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''Square str'''
        return ("[Square] (%s) %s/%s - %s" % (
            self.id,
            self.x,
            self.y,
            self.size,
            ))

    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self.width = value
        self.height = value
