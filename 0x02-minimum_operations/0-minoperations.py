#!/usr/bin/python3
""" Initialize the minimum Operations
    """


def minOperations(n: int) -> int:
    """ Initialize characters with an H """
    next = 'H'
    body = 'H'
    operations = 0
    while (len(body) < n):
        if n % len(body) == 0:
            operations += 2
            next = body
            body += body
        else:
            operations += 1
            body += next
    if len(body) != n:
        return 0
    return operations
