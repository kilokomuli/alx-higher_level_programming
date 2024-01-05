#!/usr/bin/python3
""" defines class Rectangle """


class Rectangle:
    """ represents rectangle """
    def __init__(self, width=0, height=0):
        """
        instantiates with optional width and height
        """
        self.height = height
        self.width = width

    def width(self):
        """ property to retrieve private attribute width """
        return self._width

    def width(self, value):
        """
        creates a setter for the width property
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def height(self):
        """
        property to retrieve private attrbute height
        """
        return self._height

    def height(self, value):
        """
        creates a setter for the height property
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
