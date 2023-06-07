#!/usr/bin/python3
def roman_to_int(roman_string):
    "A function that converts a roman Numeral to integer"
    dicto = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    romanInt = 0
    for letter in roman_string:
        for k, v in dicto.items():
            if k == letter:
                romanInt += v
    return romanInt
