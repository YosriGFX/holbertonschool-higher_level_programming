#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for b in matrix:
        if b:
            for a in range(len(b) - 1):
                print(end="{} ".format(b[a]))
            print("{}".format(b[a + 1]))
        else:
            print()
