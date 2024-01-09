#!/usr/bin/python3
""" Defines class Rectangle the t inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """ instantiates rectangle class
        args:
            width - width of the rectangle
            height - height of the rectangle
        Return:
            integer validated by integer validation"""
        self.__width = width
        self.__height = height
        self.integer_validator = ("width", width)
        self.integer_validator = ("height", height)

    def area(self):
        """ Returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
