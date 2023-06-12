#!/usr/bin/python3
"Task 6"


class Square:
    "Defines a square(getter, setter)"
    def __init__(self, size=0, position=(0, 0)):
        "Instantiation"
        self.__size = size
        self.__position = position
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        if self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @size.setter
    def size(self, value):
        "Setter of the size"
        self.__size = value

    def area(self):
        "Returns the square area"
        return self.__size ** 2

    def my_print(self):
        "Print method"
        if self.__size == 0:
            print()
        for newLines in range(self.__position[1]):
            if self.__position[1] >= 0:
                print()
        for columns in range(self.__size):
            for spaces in range(self.__position[0]):
                print(" ", end="")
            for rows in range(self.__size):
                print("#", end="")
            print()
