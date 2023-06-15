#!/usr/bin/python3
"Task 4"


def text_indentation(text):
    '''Prints a text with 2 new lines after each of
    these character: ".", "?" and ":"'''
    SpaceCheck = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i - 1] in {".", "?", ":"}:
            print(text[i] + "\n")
            SpaceCheck = True
        if SpaceCheck:
            if i < len(text) - 1 and text[i + 1] == " ":
                continue
            SpaceCheck = False
        else:
            print(text[i], end="")
