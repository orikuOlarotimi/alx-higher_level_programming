#!/usr/bin/python3
"""Return json format of a string"""


import json


def to_json_string(my_obj):
    """give json representation """
    return json.dumps(my_obj)
