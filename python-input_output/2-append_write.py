#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Block where open a file and write in the end of the file"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
