#!/usr/bin/python3
""" defines a retcngle """


class Rectangle:
    """ represents rectangle """
    def __init__(self, width=0, height=0):
        """instatiates class rectangle"""
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    def width(self):
        """
        property to retrieve private instance
        attribute width
        """
        return self._width

    def width(self, value):
        """
        propety setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def height(self):
        """
        retrieves private instance
        attribute width
        """
        return self._height

    def height(self, value):
        """
        property setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """
        return area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        returns the perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
