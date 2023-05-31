#!/usr/bin/python3
def remove_char_at(str, n):
    """A function that creates a copy of the string, removing the
    character at the position n"""
    nString = ""
    for i in range(len(str)):
        if i != n:
            nString = nString + str[i]
    return nString
