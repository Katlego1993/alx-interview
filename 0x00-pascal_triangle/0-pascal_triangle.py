#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    p = []
    if n <= 0:
        return p
    p = [[1]]
    for o in range(1, n):
        temp = [1]
        for q in range(len(p[o - 1]) - 1):
            curr = p[o - 1]
            temp.append(p[o - 1][q] + p[o - 1][q + 1])
        temp.append(1)
        p.append(temp)
    return p
