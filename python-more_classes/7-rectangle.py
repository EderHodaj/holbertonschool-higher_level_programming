#!/usr/bin/python3
'''
Function that defines a rectangle
'''


class Rectangle:
    '''
    Void
    '''
    number_of_instances = 0
    print_symbol = str("#")

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        new_str = ""
        if self.width == 0 or self.height == 0:
            return new_str
        else:
            for i in range(self.height):
                for j in range(self.width):
                    new_str += str(self.print_symbol)
                if i < self.height - 1:
                    new_str += "\n"
        return new_str

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
