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
