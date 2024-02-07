#!/usr/bin/python3
'''
Input output
'''


def write_file(filename="", text=""):
    '''
    Write files
    '''
    with open(filename, 'w', encoding="utf-8") as my_file:
        content = my_file.write(text)
    return len(text)
