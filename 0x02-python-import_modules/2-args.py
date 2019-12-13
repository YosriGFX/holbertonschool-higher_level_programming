#!/usr/bin/python3
import sys
if __name__ == '__main__':
    print(len(sys.argv[1:]), "arguments:")
    if len(sys.argv) != 1:
        a = 1
        for x in sys.argv[1:]:
            print(end="{}: {}\n".format(a, x))
            a += 1
