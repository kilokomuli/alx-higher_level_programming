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

    pascal = [[1]]
    while len(pascal) != n:
        tri = pascal[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        pascal.append(tmp)
    return pascal
