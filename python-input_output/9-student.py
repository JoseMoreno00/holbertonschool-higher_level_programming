#!/usr/bin/python3
"""Sry but the comment te lo debo"""


class Student:
    """Task 9"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
