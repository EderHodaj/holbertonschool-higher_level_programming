#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for index in range(0, x):
        try:
            print(my_list[index], end = "")
            count += 1
        except IndexError:
            break
    print()
    return count

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
