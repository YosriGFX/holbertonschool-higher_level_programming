#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dec = a_dictionary.copy()
    for a in new_dec:
        if a_dictionary[a] == value:
            del a_dictionary[a]
    return a_dictionary
