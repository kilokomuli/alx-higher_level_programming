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

    def to_json(self):
        """ public method that retrieves a dictionary representation of
        student instance
        Returns:
            dict: dictionary representation"""
        return self.__dict__

