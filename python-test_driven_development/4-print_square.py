#!/usr/bin/python3
"Task 3"


def print_square(size):
    "Prints a square based in its size"
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for each in range(size):
            print("#", end="")
        print()
