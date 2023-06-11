#!/usr/bin/python3
"""check if class inherited from a class"""


def inherits_from(obj, a_class):
    """check if class inherited from a class"""
    return isinstance(obj, a_class) and type(obj) != a_class
