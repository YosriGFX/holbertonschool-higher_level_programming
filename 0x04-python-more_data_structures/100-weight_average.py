#!/usr/bin/python3


def mul_in(tuple=()):
    if len(tuple) > 1:
        return tuple[0] * tuple[1]
    else:
        return 0


def last(tuple=()):
    if len(tuple) > 1:
        return tuple[1]
    else:
        return 0


def weight_average(my_list=[]):
    if my_list:
        d = 0
        s = 0
        new = list(map(mul_in, my_list))
        news = list(map(last, my_list))
        for a in new:
            s += a
        for a in news:
            d += a
        return s / d
    else:
        return 0
