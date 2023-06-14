#!/usr/bin/python3
"""A function to append to a file"""


def append_write(filename="", text=""):
    """appends a text to a  file"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
