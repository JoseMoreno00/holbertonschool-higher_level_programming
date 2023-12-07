#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”:"""


import json


def load_from_json_file(filename):
    """load from Json File"""
    with open(filename, "r", encoding="utf-8") as Jfile:
        load_obj = json.load(Jfile)
    return load_obj
