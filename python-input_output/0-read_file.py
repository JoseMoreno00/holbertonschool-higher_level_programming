#!/usr/bin/python3
"""Read a File"""


def read_file(filename=""):
    """Block that read a file and print the content"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
