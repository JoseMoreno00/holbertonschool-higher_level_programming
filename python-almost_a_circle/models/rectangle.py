#!/usr/bin/python3
"""
Define a class called Rectangle that inherits from Base

Rectangle

Class Rectangle have:
a function int, recive values {width, height, x, y, id}
set private instances attributes, whit same name and asing the value
call super class whit id, use the logic of the __init__ of the Base
"""
from .base import Base


class Rectangle(Base):
    """Define the func to set the privates instances and the super call"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function that returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Function that print the rectangle"""
        for y in range(self.__y):
            print()
        for a in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for b in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Function that print the class name and the values that have"""
        return f"[Rectangle] ({self.id}) {self.__x}\
/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Function that upgrade the instances of the class Rectangle"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Function that create a dictionary whit the value of atributes"""
        MarioDictionary = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
        return MarioDictionary
