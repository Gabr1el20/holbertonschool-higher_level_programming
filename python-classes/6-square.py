#!/usr/bin/python3
"Task 6"


class Square:
    "Defines a square(getter, setter)"
    def __init__(self, size=0, position=(0, 0)):
        "Instantiation"
        self.__size = size
        self.__position = position

    @property
    def size(self):
        "Getter of the size"
        return self.__size

    @property
    def position(self):
        "getter of position"
        return self.__position

    @position.setter
    def position(self, value):
        "Setter of position"
        self.__position = value
        if self.__position[0] is not int or self.__position[1] is not int:
            raise TypeError("position must be a tuple of 2 positive integers")

    @size.setter
    def size(self, value):
        "Setter of the size"
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        "Returns the square area"
        return self.__size ** 2

    def my_print(self):
        "Print method"
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print()
