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
    start_of_line = True

    for char in text:
        if start_of_line:
            print(char, end="")
            start_of_line = False
        else:
            if char in ".?:":
                print("", end="\n\n")
                start_of_line = True
            else:
                print(char, end="")
