#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""
"""import system"""
from sys import argv

"""import save_file from json"""
save = __import__("7-save_to_json_file").save_to_json_file
"""import load_file from json"""
load = __import__("8-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    json_list = load(filename)
except:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save(json_list, filename)
