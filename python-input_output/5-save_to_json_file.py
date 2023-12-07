#!/usr/bin/python3
"""function that writes an Object to a text file,
using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """return the JSON representation of a string object"""
    with open(filename, "w", encoding="utf-8") as Jfile:
        json.dump(my_obj, Jfile)
