#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if len(argv) == 4:
        if op == "+":
            print("{0} + {1} = {2}".format(a, b, add(a, b)))
        if op == "-":
            print("{0} - {1} = {2}".format(a, b, sub(a, b)))
        if op == "*":
            print("{0} * {1} = {2}".format(a, b, mul(a, b)))
        if op == "/":
            print("{0} / {1} = {2}".format(a, b, div(a, b)))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
