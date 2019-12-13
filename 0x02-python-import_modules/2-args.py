#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    num = len(argv)
    if num == 1:
        print("0 arguments.")
    elif num == 2:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(num - 1))
        for x in range(1, num):
            print("{:d}: {:s}".format(x, argv[x]))
