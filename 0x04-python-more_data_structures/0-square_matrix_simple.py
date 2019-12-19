#!/usr/bin/python3
def dub(lists=[]):
    new = []
    for a in lists:
        new.append(a ** 2)
    return new
def square_matrix_simple(matrix=[]):
    new = []
    for a in matrix:
        new.append(dub(a))
    return new
