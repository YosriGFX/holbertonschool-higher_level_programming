#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string.isalpha():
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(roman_string)
        total = dic[roman_string[n - 1]]
        for i in range(n - 1, 0, - 1):
            current = dic[roman_string[i]]
            prev = dic[roman_string[i - 1]]
            if prev >= current:
                total += prev
            else:
                total -= prev
        return total
    else:
        return None
