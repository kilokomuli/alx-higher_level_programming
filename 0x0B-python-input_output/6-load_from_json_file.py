#!/usr/bin/python3
""" A JSON module"""
import json


def load_from_json_file(filename):
    """ Creates an object from a JSON file
    Args:
        filename: A string representing name of a file
    Return:
         Any: Python object created from JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
