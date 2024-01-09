#!/usr/bin/python3
""" Defines a function that reads a
text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """ reads a text file and prints it to stdout
    Args:
        filename: name of the text file
        """
    with open(filename, 'r', encoding="utf-8") as file:
        read_data = file.read()
        print (read_data, end='')
