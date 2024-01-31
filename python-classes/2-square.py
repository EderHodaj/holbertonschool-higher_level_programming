#!/usr/bin/python3
'''
    We will create a class named Square
'''


class Square:
    '''
        Size must be an integer and greater than 0
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
