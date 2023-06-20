#!/usr/bin/python3
"Task 2"


def append_write(filename="", text=""):
    "Appends a str at end of a file and returns n of chars"
    with open(filename, mode='a', encoding='utf-8') as appfile:
        appfile.write(text)
    return len(text)
