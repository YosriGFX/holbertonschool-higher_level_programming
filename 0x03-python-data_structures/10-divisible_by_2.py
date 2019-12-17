#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    if my_list:
        for a in range(0, len(my_list)):
            if my_list[a] % 2 == 0:
                new += [1]
            else:
                new += [0]
    return new
