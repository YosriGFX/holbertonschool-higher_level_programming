#!/usr/bin/python3
import sys
if __name__ == '__main__':
    print("{:d} arguments:".format(len(sys.argv[1:])))
    a = 1
    for x in sys.argv[1:]:
        print(end="{}: {}\n".format(a, x))
        a += 1
