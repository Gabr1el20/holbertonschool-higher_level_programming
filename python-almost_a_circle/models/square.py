#!/usr/bin/python3
"Task 10"
from models.rectangle import Rectangle


class Square(Rectangle):
    "A square class that inherits Rectangle"
    def __init__(self, size, x=0, y=0, id=None):
        "Instantiation"
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "String representation"
        return (
            f"[Square] ({self.id}) {self.x}/{self.y}"
            f" - {self.width}"
        )

    @property
    def size(self):
        "Getter of the size"
        return self.width

    @size.setter
    def size(self, value):
        "Size setter"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
