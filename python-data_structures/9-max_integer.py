#!/usr/bin/python3
def max_integer(my_list=[]):
    count = my_list[0]
    if len(my_list) == 0:
        return None
    for element in my_list:
        if element > count:
            count = element
    return count
