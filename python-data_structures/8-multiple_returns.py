#!/usr/bin/python3
def multiple_returns(sentence):
    """A function that returns a tuple with the length
    of a string and its first character"""
    x = len(sentence)
    if len(sentence) > 0:
        latupla = (x, sentence[0])
    else:
        latupla = (x, None)
    return latupla
