#!/usr/bin/python3
'''
Inheritance exx
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Functions
    '''
    def __init__(self, size):
        Rectangle.integer_validator(self, "size",  size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
