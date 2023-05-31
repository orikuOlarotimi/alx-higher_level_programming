#!/usr/bin/python3
"""A Square Class with private attribute and validations and method"""


class Square:
    """A class that have a private attribute size and calculate the area"""
    def __init__(self, size=0):
        try:
            if size >= 0:
                self.__size = size
        except ValueError:
            raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size
