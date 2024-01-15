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

    def update(self, *args, **kwargs):
        """Assigns arguments positional and keyword to attributes"""
        if args != None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionay representation of a square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
