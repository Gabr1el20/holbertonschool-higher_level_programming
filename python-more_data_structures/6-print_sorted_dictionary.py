#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    "A function that prints a dictionary by ordered keys"
    if a_dictionary is None:
        return
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v))
