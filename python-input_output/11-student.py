#!/usr/bin/python3
"""Sry but the comment te lo debo"""


class Student:
    """Task 9"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(attrs, list):
            return self.__dict__
        else:
            dictionary = {}
            for idx in attrs:
                if idx in self.__dict__:
                    dictionary[idx] = self.__dict__[idx]
            return dictionary

    def reload_from_json(self, json):
        for point, value in json.items():
            setattr(self, point, value)
