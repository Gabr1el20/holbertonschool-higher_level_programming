#!/usr/bin/python3
def safe_print_integer(value):
    "Prints an integer with {:d}.format()"
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except Exception:
        pass
    else:
        return False
