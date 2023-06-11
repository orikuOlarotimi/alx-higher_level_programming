#!/usr/bin/python3
"""create Rectangle class and inherit from base geometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create Rectangle class and inherit
    from base geometry
    """

    def __init__(self, width, height):
        """create Rectangle class and inherit"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
