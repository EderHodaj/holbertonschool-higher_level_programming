#!/usr/bin/python3
''' Square class inherts from rectangle'''
from .rectangle import Rectangle


class Square(Rectangle):
    '''Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''str'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''size of this square'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
