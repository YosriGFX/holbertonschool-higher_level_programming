#!/usr/bin/python
def number_keys(a_dictionary):
    s = 0
    for a in a_dictionary:
        if a is not None:
            s += 1
    return s
