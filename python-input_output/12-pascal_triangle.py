#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Pascal triangle function"""
    my_list = []
    all_lists = []
    if n <= 0:
        return my_list
    else:
        for _ in range(n):
            new_list = []
            all_lists.append(new_list)

        all_lists[0] = [1]
        if n > 1:
            all_lists[1] = [1, 1]

        for idx_all in range(2, n):
            all_lists[idx_all].append(1)
            for element in range(1, idx_all):
                all_lists[idx_all].append(all_lists[idx_all-1][element-1] +
                                          all_lists[idx_all-1][element])
            all_lists[idx_all].append(1)
    return all_lists
