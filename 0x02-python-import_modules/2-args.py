#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    num = len(argv)
    if num == 1:
        print("0 arguments.")
    elif num == 2:
        print("{} argument:".format(num - 1))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(num - 1))
        for x in range(1, num):
            print("{}: {}".format(x, argv[x]))
