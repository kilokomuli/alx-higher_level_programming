#!/usr/bin/python3
""" Define class BaseGeometry"""


class BaseGeometry:
    """ BaseGeometry class witha n unimplemented area
    method"""

    def area(self):
        """Raises an exception with the message are() is not implemented"""
        raise Exception("area() is not implemented")
