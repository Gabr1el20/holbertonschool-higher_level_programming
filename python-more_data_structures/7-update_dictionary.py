#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    "A function that replaces or adds key/value in a dictionary"
    for k, v in a_dictionary.items():
        if k == key:
            a_dictionary[k] = value
        else:
            a_dictionary[key] = value
