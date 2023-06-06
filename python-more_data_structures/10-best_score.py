#!/usr/bin/python3
def best_score(a_dictionary):
    "A function that returns a key with the biggest int value"
    if a_dictionary:
        return max(a_dictionary, a_dictionary.get)
    else:
        return
