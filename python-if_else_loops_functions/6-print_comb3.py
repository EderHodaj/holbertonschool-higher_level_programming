#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        separator = ', ' if not (i == 8 and j == 9) else ''
        print("{}{}{}".format(i, j, separator), end='')

print()
