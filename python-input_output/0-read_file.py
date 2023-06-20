#!/usr/bin/python3
"Task 0"


def read_file(filename=""):
    "Reads a text file and prints it to stdout"
    with open(filename, encoding='utf-8') as fileR:
        content = fileR.read()
        print(content, end="")
