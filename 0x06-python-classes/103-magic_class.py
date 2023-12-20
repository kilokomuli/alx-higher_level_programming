#!/usr/bin/python3
""" define a magic class """


import math


class MagicClass:
    """ Magic class and its properties
    Attributes:
    Radius:radius
    """
    def __init__(self, radius):
        """ creates a new instance for magic class
        Args:
        radius: radius
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """ finds the area
        Returns: area
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        finds circumference
        returns: circumference
        """
        return 2 * math.pi * self.__radius
