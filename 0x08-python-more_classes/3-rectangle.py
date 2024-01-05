#!/usr/bin/python3
""" defines a retcngle """


class Rectangle:
    """ represents rectangle """
    def __init__(self, width=0, height=0):
        """instatiates class rectangle"""
        self.height = height
        self.width = width

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
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """
        return area of a rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
        returns the perimeter of rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

        def __str__(self):
            """
            prints the rectangele with the character #
            """
            rectangle = []
            if self._width == 0 or self._height == 0:
                return ""
        
            for i in range(self._height):
                for j in range(self._width):
                    rectangle.append("#")
                rectangle.append("\n")
            rectangel.pop()

            return "".join(rectangle)
