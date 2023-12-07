#!/usr/bin/python3
"""function that writes a string to a text file """


def write_file(filename="", text=""):
    """Block that open (or create if dont exist) a text file and write"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
