#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Returns True if the object is exactly an
    instance of the specified class; otherwise False
    args:
        obj - object of a class
        a_class - is a class
    Return:
        True if the object is excatly an
        instance of the class or otherwise False"""
    return type(obj) is a_class
