#!/usr/bin/python3
import json
import os.path
""" Defines class Base which will be "base" of all the other classe"""


class Base:
    """class base
    Attributes:
        __nb_objects = 0 which is a private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor
        Args:
            id is a public instance attribute which is assigned to None
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)
