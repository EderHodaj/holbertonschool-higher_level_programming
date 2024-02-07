#!/usr/bin/python3
'''
Input output
'''


def read_file(filename=""):
    '''
    Read files
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
