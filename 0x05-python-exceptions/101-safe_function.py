#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except (ValueError, TypeError, IndexError, ZeroDivisionError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
