#!/usr/bin/python3
'''base class'''
from .base import Base


class Rectangle(Base):
    '''constructor'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''area of rectangle'''
        return self.width * self.height

    def display(self):
        '''Print Rectangle Instance'''
        for j in range(self.y):
            print()
        for i in range(self.height):
            print("" * self.y + " " * self.x + "#" * self.width)

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        return f"[Rectangle] ({id}) {x}/{y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '''Update attributes'''
        attribute_names = ['id', 'width', 'height', 'x', 'y']
        for attr_name, new_value in zip(attribute_names, args):
            setattr(self, attr_name, new_value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        '''Class to dict'''
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return {'id': id, 'width': width, 'height': height, 'x': x, 'y': y}

