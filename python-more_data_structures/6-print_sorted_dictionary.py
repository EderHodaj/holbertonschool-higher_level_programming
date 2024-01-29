#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keys, value in sorted(a_dictionary.items()):
        print(f"{keys}: {value}")
