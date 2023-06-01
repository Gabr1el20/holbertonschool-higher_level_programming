#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = argv[1]
    b = argv[3]
    if len(argv) - 1 == 3:
        if op == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        if op == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        if op == "*":
            print("{} * {:d} = {}".format(a, b, mul(a, b)))
        if op == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))