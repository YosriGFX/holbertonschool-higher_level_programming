#!/usr/bin/python3
'''Finds a peak in a list'''


def find_peak(list_of_integers):
    '''Finds a peak in a list'''
    if not list_of_integers:
        return
    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    peak = list_of_integers[1]
    a = 1
    while a < length:
        if peak < list_of_integers[a]:
            peak = list_of_integers[a]
        a += 1
    return peak
