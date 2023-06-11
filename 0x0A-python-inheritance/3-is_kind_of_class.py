#!/usr/bin/python3
"""check if both class are kind of the same"""


def is_kind_of_class(obj, a_class):
    """check if both class are kind of are the same"""
    if isinstance(obj, a_class):
        return True
    return False
