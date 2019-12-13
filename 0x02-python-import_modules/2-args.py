#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    num = len(argv)
    print("{:d} arguments:".format(num - 1))
    for i, arg in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, arg))
