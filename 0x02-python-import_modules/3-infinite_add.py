#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = 0
    for a in argv:
        if a != argv[0]:
            x += int(a)
    print(x)
