#!/usr/bin/python3
""" defines function inherits_from """


def inherits_from(obj, a_class):
    """  returns True if the object is an instance of a
    class that inherited (directly or indirectly) from
    the specified class ; otherwise False.
    args:
        obj: object of the class
        a_class: class
        Return:
            true if aan object is an instance of a class
            otherwise False"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
