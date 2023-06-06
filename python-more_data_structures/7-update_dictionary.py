#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    "A function that replaces or adds key/value in a dictionary"
    for k, v in a_dictionary.items():
        if k == key:
            v = value
        else:
            a_dictionary[key] = value
