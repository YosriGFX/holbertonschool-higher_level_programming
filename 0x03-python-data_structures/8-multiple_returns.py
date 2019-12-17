#!/usr/bin/python3
def multiple_returns(sentence):
    countain = (0, None)
    if sentence:
        l = len(sentence)
        f = sentence[0]
        countain = (l, f)
    return countain
