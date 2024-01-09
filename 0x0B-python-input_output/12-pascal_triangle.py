#!/usr/bin/python3
""" define function pascal_triangle"""


def pascal_triangle(n):
    """ Returns alist of lists of integers representing the pascal's triangle
    of n
    args:
       n: represents the pascal triangle
    returns:
        lists of lists representing pascal's triangle"""

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for i in range(n - 1):
        triangle.append([x + n for x, n in zip(triangle[-1] + [0],
                                             [0] + triangle[-1])])
        return (triangle)
