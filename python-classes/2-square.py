#!/usr/bin/python3
"Task 2"


class Square:
    "Defines a square"
    def __init__(self, size=0):
        "Instantiation"
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
