#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor
        Attributes:
            width private instace attribute with public setter and getter
            height private instace attribute with public setter and getter
            x private instace attribute with public setter and getter
            y private instace attribute with public setter and getter
            """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width retriver"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width property setter
       Rasies:
           TypeError: if width is not an integr
           ValueError: if width is <= 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height retriever"""
        return self.__height

    @height.setter
    def height(self, value):
        """height property setter
        Raises:

            TypeError: if height is not an integer
            ValueError: if width is less than zero"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x retiever"""
        return self.__x

    @x.setter
    def x(self, value):
        """Property setter for x.

        Args:
            value: x.

        Raises:
            TypeError: if x is not an integer.
            ValueError: if x is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y retriever"""
        return self.__y

    @y.setter
    def y(self, value):
        """Property setter for y.

        Args:
            value: y.

        Raises:
            TypeError: if y is not an integer.
            ValueError: if y is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area value of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the rectangle instance with the character #"""
        if self.__y > 0:
            for i in range(self.__y):
                print()
            self.__y = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__y == j:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()

    def __str__(self):
        """ overrides the rectangle"""
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    def update(self, *args, **kwargs):
        """Assign arguments to each attribute in order id, width, height,
        x, y
        Parameter:
        args:arguments
        kwargs: double pointer to a dictionary"""
        if args is not None and len(args) is not 0:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atrr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
