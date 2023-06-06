#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    "A function that finds all multiples of 2 in a list"
    newList = []
    for x in my_list:
        if (x % 2) == 0:
            newList += [True]
        else:
            newList += [False]
    return newList
