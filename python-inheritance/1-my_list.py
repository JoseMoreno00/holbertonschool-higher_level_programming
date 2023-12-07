#!/usr/bin/python3
"""Class that define a list whit a functiuon that print the list sorted"""


class MyList(list):
    """print the list sorted"""
    def print_sorted(self):
        print(sorted(self))
