#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]] and matrix != []:
        for b in range(len(matrix)):
            for a in range(len(matrix) - 1):
                print(end="{} ".format(matrix[b][a]))
            print("{}".format(matrix[b][a + 1]))
    else:
        print()
