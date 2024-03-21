#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """Calculate fewest no. of operations needed to result in n H characters"""
    t = 0
    m = 2
    while n > 1:
        while not n % m:
            t += m
            n /= m
        m += 1
    return t
