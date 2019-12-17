#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for b in matrix:
        if b:
            for a in range(len(b)):
                print(end="{}".format(b[a]))
                if a == (len(b) - 1):
                    print("")
                else:
                    print(end=" ")
        else:
            print("")
