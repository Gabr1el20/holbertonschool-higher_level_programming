#!/usr/bin/python3
def safe_print_integer_err(value):
    'Prints an integer'
    import sys
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            print("{:d}".format(value))
            return False
    except ValueError as e:
        print("Exception: {}".format(e), file=sys.stderr)
