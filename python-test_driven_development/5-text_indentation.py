#!/usr/bin/python3
"Task 4"


def text_indentation(text):
    '''Prints a text with 2 new lines after each of
    these character: ".", "?" and ":"'''
    checker = False
    for i in range(len(text)):
        if text[i - 1] in [".", ":", "?"]:
            print()
            print()
            checker = True
        if checker:
            if i < len(text) - 1 and text[i + 1]:
                continue
            checker = False
        else:
            print(text[i], end="")
