#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
        except IndexError:
            raise
    print("")
    return count
