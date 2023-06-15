#!/usr/bin/python3
"Task 1 of more_classes"


class Rectangle():
    "Defines a rectangle (based on 0-rectangle.py)"
    def __init__(self, width=0, height=0):
        "Instantiation"
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise TypeError("width must be >= 0")
        if height < 0:
            raise TypeError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        "Getter of the width"
        return self.__width

    @property
    def height(self):
        "Getter of the height"
        return self.__height

    @height.setter
    def height(self, value):
        "Setter of the height"
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        "Setter of the width"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value
