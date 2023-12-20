#!/usr/bin/python3
""" define a magic class """
import math


class MagicClass:
    """ Magic class and its properties
    Attributes:
    Radius:radius
    """
    def __init__(self, radius=0):
        """ creates a new instance for magic class
        Args:
        radius: radius
        """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
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
