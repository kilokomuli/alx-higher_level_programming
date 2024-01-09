#!/usr/bin/python3
""" defines function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file, after each line conatining a
    specific string.
    Args:
        filename: name of the file
        Search_string: specific string to search for in each line
        new_string: line of text to insert after each line containing
        the search string
    Return: none
    """
    with open(filename, "r") as file:
        text = file.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
