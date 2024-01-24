#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []

    for element in my_list:
        if element % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1