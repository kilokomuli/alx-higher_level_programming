#!/usr/bin/python3
""" function is_same_class"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an
    instance of the specified class; otherwise False
    args:
        obj - object of a class
        a_class - is a class
    Return:
        True if the object is excatly an
        instance of the class or otherwise False"""
    return type(obj) == a_class
