#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """A function that returns a new dictionary with all values
    multiplied by 2"""
    if a_dictionary is None:
        print("Dictionary is None")
        return
    dicto = {k: v*2 for k, v in a_dictionary.items()}
    return dicto
