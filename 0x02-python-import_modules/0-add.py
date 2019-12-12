#!/usr/bin/python3
__import__("add_0")
from add_0 import add
if __name__ == '__main__':
    a = 1
    b = 2
    s = add(a, b)
    print("{} + {} = {}".format(a, b, s))