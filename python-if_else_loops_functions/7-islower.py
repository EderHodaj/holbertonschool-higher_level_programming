#!/usr/bin/python3
def islower(c):
    while True:
        if ord(c) in range(ord('a'), ord('z') + 1):
            return True
        else:
            return False
