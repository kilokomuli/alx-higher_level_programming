#!/usr/bin/python3
""" Module presenting json to perform JSON serialization"""
import json


def to_json_string(my_obj):
    """ Returns the JSON representation of an object as a string.
    Args:
        my_obj: any python object
    Return:
        str: JSON represantation fo the object"""
    return json.dumps(my_obj)
