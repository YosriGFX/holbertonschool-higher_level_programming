#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    lon = len(argv)
    b = 0
    if lon > 3:
        for a in range(1, lon):
            b += int(argv[a])
    elif lon == 3:
        b = int(argv[1]) + int(argv[2])
    elif lon == 2:
        b = int(argv[1])
    print("{:d}".format(b))
