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

    start_of_line = True  # To track whether we are at the beginning of a line

    for char in text:
        if start_of_line:
            print(char, end="")
            start_of_line = False
        else:
            if char in ".?:":  # Check if the character is '.', '?', or ':'
                print("", end=" ")  # Add a space after the punctuation
                print("", end="\n\n")  # Print two newlines
                start_of_line = True  # Next character will be at the beginning of a line
            else:
                print(char, end="")
