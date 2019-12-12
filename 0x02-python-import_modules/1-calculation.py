#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    a = 10
    b = 5
    ea = "{} + {}".format(a, b)
    sa = add(a, b)
    es = "{} - {}".format(a, b)
    ss = sub(a, b)
    em = "{} * {}".format(a, b)
    sm = mul(a, b)
    ed = "{} / {}".format(a, b)
    sd = div(a, b)
    print("{} = {:d}".format(ea, sa))
    print("{} = {:d}".format(es, ss))
    print("{} = {:d}".format(em, sm))
    print("{} = {:d}".format(ed, sd))
