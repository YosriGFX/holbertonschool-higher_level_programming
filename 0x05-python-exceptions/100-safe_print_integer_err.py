#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, NameError):
        return False
    except ValueError as e:
        print("Exception: {}".format(e))
        return False
