#!/usr/bin/python3
def safe_function(fct, *args):
    'Executes a function safely'
    import sys
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
