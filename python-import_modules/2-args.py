#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = len(argv) - 1
    if i > 1:
        print("{} arguments:".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    elif i == 0:
        print("{} arguments.".format(i))
    for i in range(1, len(argv)):
        print("{0}: {1}".format(i, argv[i]))
