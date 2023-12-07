#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Class define a square"""
    def __init__(self, size=0, position=(0, 0)):

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not all(isinstance(idx, int) for idx in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(idx >= 0 for idx in position):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not all(isinstance(idx, int) for idx in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(idx >= 0 for idx in position):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return None
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
