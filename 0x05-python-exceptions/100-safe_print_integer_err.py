#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except TypeError:
        sys.stderr.write("Exception: TypeError")
        return (False)
