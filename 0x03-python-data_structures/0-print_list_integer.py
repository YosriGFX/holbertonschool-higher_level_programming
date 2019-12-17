#!/usr/bin/python3
def print_list_integer(my_list=[]):
    a = 0;
    while my_list[a]:
        print("{:d}".format(my_list[a]))
        a += 1;
