#!/usr/bin/python3
"""Defines an object attribute lookup function that returns a list of  of methods of an object."""


def lookup(obj):
    """Return a list of an object's available attributes in a list."""
    return dir(obj)
