#!/usr/bin/python3
""" Finds a peak in alist of unsorted integers """


def find_peak(list_of_integers):
    """function to find the peak"""
    highest = None
    for x in list_of_integers:
        if highest is None or highest < x:
            highest = x
    return highest
