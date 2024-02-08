#!/usr/bin/python3
'''
Input output
'''


import json


def to_json_string(my_obj):
    json_string = json.dumps(my_obj)
    print(json_string)
