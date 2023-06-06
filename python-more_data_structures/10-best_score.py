#!/usr/bin/python3
def best_score(a_dictionary):
    "A function that returns a key with the biggest int value"
    if a_dictionary is None:
        return
    else:
        maxValue = max(a_dictionary)
        maxKey = max(a_dictionary, key=a_dictionary.get)
        return maxKey
