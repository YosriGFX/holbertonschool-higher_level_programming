#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    num = len(argv)
    print("{:d} {}{}".format(num - 1, "argument"
                             if num - 1 == 1 else "arguments", "."
                             if num == 1
                             else ":"))
    for i, arg in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, arg))
