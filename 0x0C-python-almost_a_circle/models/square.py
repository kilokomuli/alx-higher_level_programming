#!/usr/bin/python3
"""import module Rectangle and define class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes class square
        Args:
            size: size of the square
            x: Default to 0
            Y: default to 0
            id: identifies the number of squares defult to None"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Prints the square"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """retrievs size property"""
        return self.width

    @size.setter
    def size(self, value):
        """property
        Args:
            value: width of the square"""
        self.width = value
        self.height = value
