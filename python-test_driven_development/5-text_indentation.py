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
    for i in text:
        print(i, end="")
        if i == "." or i == "?" or i == ":":
            print("", end="\n\n")
