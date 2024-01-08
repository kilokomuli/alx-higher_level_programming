#!/usr/bin/python3
""" define class MyList that inherits from list
"""


class MyList(list):
    """ custom list class that
    inherits  from the built-in list.
    public method:
    print_sorted(self - prints the list
    but in ascending orde"""

    def print_sorted(self):
        """ prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
