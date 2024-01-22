#!/usr/bin/python3
for index in range(97, 123):
    if index == 113 or index == 101:
        continue
    else:
        print("{}".format(chr(index)), end="")
