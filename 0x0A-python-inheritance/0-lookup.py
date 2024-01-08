#!/usr/bin/python3
""" lookup function
"""


def lookup(obj):
    """
    lists all available
    attributes and methods of an object
    Args:
    obj - any python object
    Return:
    lists available and methods of an
    object
    """
    return dir(obj)
