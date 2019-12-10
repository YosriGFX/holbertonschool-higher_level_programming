#!/usr/bin/python3
def uppercase(str):
    for a in range(len(str)):
        b = ord(str[a])
        if b >= 97 and b <= 123:
            b -= 32
        print(end="{}".format(chr(b)))
    print()
