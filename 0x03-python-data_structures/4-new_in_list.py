#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return copy
    if idx > len(my_list):
        return copy
    else:
        copy = []
        copy[:] = my_list[:]
        copy[idx] = element
        return copy
