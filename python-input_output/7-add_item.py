#!/usr/bin/python3
"""Name of the JSON file to work with is add_item.json"""
import sys


SaveFile = __import__('5-save_to_json_file')
LoadFile = __import__('6-load_from_json_file')

"""Load the JSON file and save the arguments to it"""
filename = "add_item.json"
try:
    my_list = LoadFile.load_from_json_file(filename)
except Exception:
    my_list = []
for idx in range(1, len(sys.argv)):
    my_list.append(sys.argv[idx])
SaveFile.save_to_json_file(my_list, filename)
