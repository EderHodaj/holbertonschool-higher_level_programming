#!/usr/bin/python3
'''
Input output
'''


def append_write(filename="", text=""):
    '''
    Write files
    '''
    with open(filename, 'a', encoding="utf-8") as my_file:
        content = my_file.write(text)
    return len(text)
