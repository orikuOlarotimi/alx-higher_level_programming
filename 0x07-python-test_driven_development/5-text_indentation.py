#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text: the string to print
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for char in ".?:":
        text = (char + "\n\n").join(
            [sen.strip(" ") for sen in text.split(char)])
    print(text, end="")


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/5-text_indentation.txt")
