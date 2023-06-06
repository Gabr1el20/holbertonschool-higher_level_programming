#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """A function that replaces all occurrences of an element
    by another in a new list"""
    newList = my_list.copy()
    for x in range(len(newList)):
        if newList[x] == search:
            newList[x] = replace
    return newList
