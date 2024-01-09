#!/usr/bin/python3
""" Defines function append_write"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file (utf8)
    and returns the number of characters added
    Args:
        filename: string representing name of the file
        text: represents characters to be added
    Return:
          number of characters added"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
