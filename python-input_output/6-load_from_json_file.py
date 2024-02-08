#!/usr/bin/python3
'''
Input output
'''


import json


def load_from_json_file(filename):
    '''
    Json File to data structure
    '''
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
        print(data)
