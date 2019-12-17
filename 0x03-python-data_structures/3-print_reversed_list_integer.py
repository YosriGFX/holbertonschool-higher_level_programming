#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for a in range(len(my_list)):
            if a != 0:
                print("{:d}".format(my_list[-a]))
    print("{:d}".format(my_list[0]))
