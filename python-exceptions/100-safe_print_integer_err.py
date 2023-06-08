#!/usr/bin/python3
def safe_print_integer_err(value):
    'Prints an integer'
    try:
        print("{:d}".format(value))
    except ValueError as e:
        print("Exception: {}".format(e))
        return False
    else:
        return True
