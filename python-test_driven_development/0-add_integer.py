#!/usr/bin/python3
"Task 0"


def add_integer(a, b=98):
    "Adds 2 integer"
    if a == float('inf') or a == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer.")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
