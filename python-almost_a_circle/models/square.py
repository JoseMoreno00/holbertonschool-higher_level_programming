#!/usr/bin/python3
"""
Define a class called Square that inherits from Rectangle

Square

Class Square have:
a function init, recive values {size, x, y, id}
set private instances attributes, whit same name and asing the value
call super class whit logical of rectangle for values recived
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Function __init__"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Function that print the class name and the values that have"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Function that upgrade the instances of the class Square"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Function that create a dictionary whit the value of atributes"""
        LuigiDictionary = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
        return LuigiDictionary
