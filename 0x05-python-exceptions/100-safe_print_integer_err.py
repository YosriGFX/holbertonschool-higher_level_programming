#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (NameError, TypeError, ValueError) as e:
        print("Exception: {}".format(e))
        return False
