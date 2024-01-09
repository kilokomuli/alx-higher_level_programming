#!/usr/bin/python3
""" A module representing JSON to perform JSON deserialization"""
import json


def from_json_string(my_str):
    """ Returns an object represented by a JSON string
    Args:
        my_str:JSON-formatted string
    Returns:
        any: Python object represented by the JSON string."""
    return json.loads(my_str)
