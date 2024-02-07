#!/usr/bin/python3

def inherits_from(obj, a_class):
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
