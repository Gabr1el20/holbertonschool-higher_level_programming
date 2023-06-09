#!/usr/bin/python3
"Task 7"


class BaseGeometry():
    "Class basegeometry, with def area(self)"
    def area(self):
        "Raises an exception"
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
