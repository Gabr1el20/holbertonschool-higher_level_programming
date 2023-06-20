#!/usr/bin/python3
"Task 1"


class MyList(list):
    "A class MyList that inherits from list"
    def print_sorted(self):
        "Prints the list, but sorted"
        print("{}".format(sorted(self)))
