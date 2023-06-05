#!/usr/bin/python3
def element_at(my_list, idx):
    "A function that retrieves an element from a list"
    if idx < 0:
        return
    elif idx > len(my_list):
        return
    x = my_list[idx]
    return x
