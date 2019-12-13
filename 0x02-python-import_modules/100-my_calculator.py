#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == '__main__':
    leng = len(argv)
    if leng != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        s = 0
        a = int(argv[1])
        b = argv[2]
        c = int(argv[3])
        if b == "+":
            s = add(a, c)
        if b == "-":
            s = sub(a, c)
        if b == "*":
            s = mul(a, c)
        if b == "/":
            s = div(a, c)
        if s == 0:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            print("{} {} {} = {}".format(a, b, c, s))
