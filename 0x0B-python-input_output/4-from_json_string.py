#!/usr/bin/python3
"""Return Json format of a string"""


import json


def from_json_string(my_str):
    """load json string in json format in a func"""
    return json.loads(my_str)
