#!/usr/bin/python3
""" Define class BaseGeometry"""


class BaseGeometry:
    """ BaseGeometry class witha n unimplemented area
    method"""

    def area(self):
        """Raises an exception with the message are() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the value to be an integer and greaterhan 0
        Args:
            name: a string representing name of the value
            Value: the value to be validated
        Raises:
            TypeError: if value is not an integer
            ValueError: if the value is less then or equal to 0"""
        if not isinstance(value, int):
            raise TypeError("name must be an integer")
        if value <= 0:
            raise ValueError("name must be greater than 0")


class Rectangle(BaseGeometry):
    """ class Rectangle inheriting from BaseGeometry
    with objects withd and heigh"""
    def __init__(self, width, height):
        """ initializes a Rectangle instance with width and height
        Args:
            width: posiitive integer representing width
            height: positive integer representing height
            """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
