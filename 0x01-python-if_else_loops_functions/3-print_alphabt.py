#!/usr/bin/python3
a = 97
while a < 123:
    if not ((a == 101) or (a == 113)):
        print(end="{}".format(chr(a)))
    a += 1
