#!usr/bin/python3
"""Define function add_inter
Attributes:
    add_integer: function that adds two integers
Parameters:
    a and b=98 must be either float or integer"""


def add_integer(a, b=98):
    """ add_integer function adds 2 integers 
    a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
