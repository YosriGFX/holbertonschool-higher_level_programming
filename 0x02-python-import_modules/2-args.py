#!/usr/bin/python3
import sys
if __name__ == '__main__':
    num = len(sys.argv[1:])
    print("{:d} arguments:".format(num))
    for x in range(1, num + 1):
        print(end="{}: {}\n".format(x, sys.argv[x]))
