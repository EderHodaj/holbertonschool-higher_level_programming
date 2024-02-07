#!/usr/bin/python3
'''
Inheritance exx
'''


def inherits_from(obj, a_class):
    '''
    Functions
    '''
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
