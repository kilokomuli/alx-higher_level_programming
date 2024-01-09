#!/usr/bin/python3
"""Defines class MyInt"""


class MyInt(int):
    """ class MyInt that inherits from int
    with inverted == and != operators"""

    def __eq__(self, other):
        """ Inverts the == operator
        Args:
            other: value to compare
        Returns:
            bool: true if self is not equal to other, otherwise False
            """
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts != operator
        Args:
           other: value to compare
        Returns:
           bool: True if self is equal to other, false otherwise
        """
        return super().__eq__(other)
