#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    lon = len(argv)
    b = 0
    for a in argv[1:]:
        b += int(a)
    print("{:d}".format(b))
