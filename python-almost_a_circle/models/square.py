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

    def update(self, *args, **kwargs):
        '''Update attributes'''
        attribute_names = ['id', 'size', 'x', 'y']
        for attr_name, new_value in zip(attribute_names, args):
            setattr(self, attr_name, new_value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        '''Class to dict'''
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return {'id': id, 'size': size, 'x': x, 'y': y}
