#!/usr/bin/python3
"""Imprting json module to perform JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file, using a JSON
    representation
    Args:
         my_obj: object to be serialized to a textfile
         filename: string representing the name of a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        json_object = json.dumps(my_obj)
        file.write(json_object)
        file.close()
