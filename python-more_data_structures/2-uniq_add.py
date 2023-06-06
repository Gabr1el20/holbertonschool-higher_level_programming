#!/usr/bin/python3
def uniq_add(my_list=[]):
    "A function that adds all unique integers in a list"
    sum = 0
    test = set(my_list)
    for x in test:
        sum += x
    return sum
