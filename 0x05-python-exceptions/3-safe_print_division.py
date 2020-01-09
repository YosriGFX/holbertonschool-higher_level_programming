#!/usr/bin/python3
def safe_print_division(a, b):
    s = 0
    try:
        s = a / b
        return s
    except ZeroDivisionError:
        s = None
    finally:
        print("Inside result: {}".format(s))
