#!/usr/bin/python3
"Task 4"


class Square:
    "Defines a square(getter, setter)"
    def __init__(self, size=0):
        "Instantiation"
        self.__size = size

    @property
    def size(self):
        "Getter of the size"
        return self.__size

    @size.setter
    def size(self, value):
        "Setter of the size"
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        "Returns the square area"
        return self.__size ** 2
