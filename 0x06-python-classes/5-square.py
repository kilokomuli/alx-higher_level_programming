#!/usr/bin/python3
""" Define class square """


class Square:
    """
    class square and its properties
    Attributes:
    size: size of the square
    """
    def __init__(self, size=0):
        """Creates new instances of square.

        Args:
            size: size of the square (1 side).
        """
        self.__size = size

    def area(self):
        """ calculates and  returns the size
        of the square """
        return Self.__size ** 2

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))
