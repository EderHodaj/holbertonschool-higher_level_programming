#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as my_file:
        contetnt = my_file.write(text)
    return len(text)
