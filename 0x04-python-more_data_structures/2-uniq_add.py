#!/usr/bin/python3


def uniqf(my_list=[]):
    uniq = []
    for a in my_list:
        if a not in uniq:
            uniq.append(a)
    return uniq


def uniq_add(my_list=[]):
    uniq = uniqf(my_list)
    s = 0
    for a in uniq:
        s += a
    return s
