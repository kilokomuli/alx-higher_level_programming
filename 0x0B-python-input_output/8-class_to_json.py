#!/usr/bin/python3
""" defines function class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for json serialization of an object
    Args:
        obj: an instance of a class
    Return:
        dict: Dictionary representation of the object serializable attributes
        """
    return obj.__dict__
