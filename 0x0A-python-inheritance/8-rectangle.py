#!/usr/bin/python3
""" Define class BaseGeometry with an unimplemendted area"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
