#!/usr/bin/python3
"Task 3"


def is_kind_of_class(obj, a_class):
    '''Returns True if the obj is an instance of, or
    if the obj is an instance of a class that inherited from
    the specified class, otherwise returns False'''
    return isinstance(obj, a_class)
