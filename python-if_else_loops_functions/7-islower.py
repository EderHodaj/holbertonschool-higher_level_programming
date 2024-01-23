#!/usr/bin/python3
def islower(c):
    for letter in c:
        letter = ord(letter)
        if letter >= 97 and letter <= 122:
            return True
        else:
            return False

