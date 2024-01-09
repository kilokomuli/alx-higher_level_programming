#!/usr/bin/python3
""" Defines class Square inheriting from class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square thet inherits from Rectangle"""
    def __init__(self, size):
        """ instatiates Square class with size
        args:
            size - size of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Returns a string represntation of the square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Returns area of square"""
        return self.__size ** 2
