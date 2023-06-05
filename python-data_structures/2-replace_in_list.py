#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    "A function that replaces an element of a list at a spec position"
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
