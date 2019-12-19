#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    sum = 0
    convert = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    for curr, nxt in zip(roman_string, roman_string[1:]):
        if convert[curr] >= convert[nxt]:
            sum += convert[curr]
        else:
            sum -= convert[curr]
    sum += convert[roman_string[-1]]
    return sum
