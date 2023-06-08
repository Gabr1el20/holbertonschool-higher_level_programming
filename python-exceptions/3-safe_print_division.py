#!/usr/bin/python3
def safe_print_division(a, b):
    'Divides 2 integers and prints the result'
    d1v = 0
    try:
        d1v = a / b
    except ZeroDivisionError:
        d1v = None
    finally:
        print("Inside result: {}".format(d1v))
        return d1v
