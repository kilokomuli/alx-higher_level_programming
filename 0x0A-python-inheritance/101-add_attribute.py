#!/usr/bin/python3
""" Adds new attribute to an object if its possible"""


def add_attribute(obj, name, value):
    """  Adds new attribute
    Args:
        obj - any python object
        name: string representing the name of the new attribute
        value: value of the new attribute
    Rasises:
          TypeError: with the message can't add new attribute
          if the object cna't have a new attribute
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    obj.__dict__[name] = value
