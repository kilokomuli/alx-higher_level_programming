#!/usr/bin/python3
""" Defines class Base which will be "base" of all the other classe"""


class Base:
    """class base
    Attributes:
        __nb_objects = 0 which is a private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor
        Args:
            id is a public instance attribute which is assigned to None
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
