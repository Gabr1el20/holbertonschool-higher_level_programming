#!/usr/bin/python3
def print_last_digit(number):
    "A function that print the last digit of a number"
    lastD = abs(number) % 10
    print("{:d}".format(lastD), end='')
    return lastD
