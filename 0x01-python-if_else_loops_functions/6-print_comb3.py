#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a < b and (a != 8 and a != 9):
            print(end="{}{}, ".format(a, b))
print("89")
