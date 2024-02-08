#!/usr/bin/python3
'''
Input output
'''


import json


def save_to_json_file(my_obj, filename):
    '''
    Json File to data structure
    '''
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
