#!/usr/bin/python3
"Task 1"
from models.base import Base


class Rectangle(Base):
    "Class Rectangle that inherits from Base"
    def __init__(self, width, height, x=0, y=0, id=None):
        "Instantiation"
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        "Width getter"
        return self.__width

    @property
    def height(self):
        "Height getter"
        return self.__height

    @property
    def x(self):
        "x getter"
        return self.__x

    @property
    def y(self):
        "y setter"
        return self.y

    @width.setter
    def width(self, value):
        "Width setter"
        self.__width = value

    @height.setter
    def height(self, value):
        "Height setter"
        self.__height = value

    @x.setter
    def x(self, value):
        "x setter"
        self.__x = value

    @y.setter
    def y(self, value):
        "y setter"
        self.__y = value
