#!/usr/bin/python3
""" Defines a function write file """


def write_file(filename="", text=""):
    """ Writes a Stringg to a textfile(UTF*) and returns the number of
    characters written
    Args:
        filename: a string representing the name of the file
        text: charcters written
    Return:
        number of characters written"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
