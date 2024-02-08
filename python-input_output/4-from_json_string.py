#!/usr/bin/python3
'''
Input output
'''


import json


def from_json_string(my_str):
    '''
    Json File to data structure
    '''
    return json.loads(my_str)
