#!/usr/bin/python3
""" define function say_my_name"""


def say_my_name(first_name, last_name=""):
    """ Prints My name is <first name> <last name>
    Args:
       first_name: represnets first name
       last_name: last name
    Return:
       string representing first and last name
    Raise:
        TypeError: if first and last name are not strings
        """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
