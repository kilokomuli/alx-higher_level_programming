#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Defines properties of rectangle
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.
        with optionals width and height

        Args:
            width : width of rectangle. Defaults to 0.
            height : height of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width retriver.
        """
        return self.__width

    @property
    def height(self):
        """Height retriver.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Args:
            value : width properties of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height of recyangle.

        Args:
            value : height properties of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
