#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for b in matrix:
        for a in range(len(b)):
            print(end="{}".format(b[a]))
            if a != (len(b) - 1):
                print(end=" ")
        print("")
