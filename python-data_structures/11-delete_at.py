#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    "A function that deletes the item at a specific position in a list"
    copyL = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return copyL
    del my_list[idx]
    return my_list
