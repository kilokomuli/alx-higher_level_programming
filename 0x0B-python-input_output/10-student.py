#!/usr/bin/python3
""" Defines class Student"""


class Student:
    """ class Student with public instance attributes
    Attr:
        first_name: representing first name
        last_name: representing last name
        age: representing age"""
    def __init__(self, first_name, last_name, age):
        """ instatiates class Student.
        Args:
            first_name: represents first_name of the student
            last_name: represents last_name of the student
            age: represents age of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ public method that retrieves a dictionary representation of
        student instance
        Args:
           attrs: list of a string
        Returns:
            dict: dictionary representation"""
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict
