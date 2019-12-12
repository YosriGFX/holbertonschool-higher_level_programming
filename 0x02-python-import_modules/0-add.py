#!/usr/bin/python3
__import__("add_0")
from add_0 import add
def _print(a, b, c):
    s = add(a, b)
    print("{} + {} = {}".format(a, b, s))
if __name__ == '__main__':
    _print(1, 2, 3)