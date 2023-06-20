#!/usr/bin/python3
"Task 1"


def write_file(filename="", text=""):
    "Writes a string to a file and returns the n of chars written"
    with open(filename, mode='w', encoding='utf-8') as Wfile:
        Wfile.write(text)
    return len(text)
