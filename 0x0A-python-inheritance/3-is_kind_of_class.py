#!/usr/bin/python3
""" defines a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """ Returns True if the object is an instance of,
    or if the onject is an instance of a class that inherited
    from, the specified
    class: otherwise false
    args:
        obj - object of the class
        a_class - the class
    Return:
        True if the object is an instance of,or if the object
        is an instance of a class inherited : otherwise False"""
    return isinstance(obj, a_class)
