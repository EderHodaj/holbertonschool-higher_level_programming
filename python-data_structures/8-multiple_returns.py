#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) < 1:
        sentence[0] = None
    new_tuple = (len(sentence), sentence[0])
    return new_tuple
