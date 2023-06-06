#!/usr/bin/python3
def max_integer(my_list=[]):
    "A function that finds the biggest integer of a list"
    if len(my_list) == 0:
        return
    biggest = None
    for comparator in my_list:
        if biggest is None or biggest < comparator:
            biggest = comparator
    return biggest
