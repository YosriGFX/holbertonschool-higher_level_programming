#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dic = {}
    for a in a_dictionary:
            mul_dic[a] = a_dictionary[a] * 2
    return mul_dic
