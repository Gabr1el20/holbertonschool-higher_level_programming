#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    "A function that prints all integers of a list, in reverse order"
    for x in reversed(range(len(my_list))):
        print("{}".format(my_list[x]))
