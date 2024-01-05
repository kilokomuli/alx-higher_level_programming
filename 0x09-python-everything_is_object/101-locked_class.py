#!/usr/bin/python3
"""
defines lockedClass
"""


class LockedClass:
    """
    it is a no class or object attribute, that prevents the user
    from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name 
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """ instantiates class LockedClass """
        self.first_name = "first_name"
