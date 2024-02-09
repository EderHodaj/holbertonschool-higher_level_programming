#!/usr/bin/python3
'''
Input output
'''


import json


def class_to_json(obj):
    '''
    Class object to json
    '''
    return obj.__dict__
