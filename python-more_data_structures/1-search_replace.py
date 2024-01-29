#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_lists = []
    for el in my_list:
        if el == search:
            new_lists.append(replace)
        else:
            new_lists.append(el)
    return new_lists
