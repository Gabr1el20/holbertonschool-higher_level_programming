#!/usr/bin/python3
def no_c(my_string):
    "A function that removes all characters c and C from a string"
    newstring = ""
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        else:
            newstring += x
    return newstring
