#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i == j or i > j:
            continue
        elif j == 9 and i == 8:
            print(f"{i}{j}")
        else:
            print(f"{i}{j}", end=", ")
