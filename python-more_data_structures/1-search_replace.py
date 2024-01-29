#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_lists = []
    for el in my_list:
        if el == search:
            new_lists.append(replace)
        else:
            new_lists.append(el)
    return new_lists

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)