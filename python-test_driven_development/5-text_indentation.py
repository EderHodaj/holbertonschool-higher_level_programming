#!/usr/bin/python3
'''
Testing excercises
'''


def text_indentation(text):
    '''
    Function that prints text with two newlines
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print("\n\n", end='')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
