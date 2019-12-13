#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    num = len(argv)
    if num == 1:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(num - 1))
        for x in range(1, num):
            print(end="{}: {}\n".format(x, argv[x]))
