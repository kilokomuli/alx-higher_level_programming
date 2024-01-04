#!/usr/bin/python3
""" defines class Rectangle """


class Rectangle:
    """ represents rectangle """
    def __init__(self, width=0, height=0):
        """
        instantiates with optional width and height
        """
        self.width = width
        self.height = height

    def width(self):
        """ property to retrieve private attribute width """
        return self.__width

    def width(self, value):
        """
        creates a setter for the width property
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """
        property to retrieve private attrbute height
        """
        return self.__height

    def height(self, value):
        """
        creates a setter for the height property
        """
        if not isinstance(valu, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
