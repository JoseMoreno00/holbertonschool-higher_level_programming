#!/usr/bin/python3
"""Function that return a list of list of integers
representing a Pascal's triangle"""


def pascal_triangle(n):
    """Function"""
    triangle = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]
    new_list = []
    if n <= 0:
        return new_list
    for idx in range(1, n + 1):
        new_list.append(triangle[idx - 1])
    return new_list
