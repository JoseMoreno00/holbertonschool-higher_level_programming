#!/usr/bin/python3
"""Def a function to check the class and inherited"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of, or if
    the object is an instance of a class that inherited from, the specified
    class ; otherwise False"""
    if not isinstance(obj, a_class):
        return False
    return True
