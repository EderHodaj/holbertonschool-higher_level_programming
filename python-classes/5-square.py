#!/usr/bin/python3
'''
    We will create a class named Square
'''


class Square:
    '''
        Size must be an integer and greater than 0
    '''
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.size):
            print("#" * self.size)
