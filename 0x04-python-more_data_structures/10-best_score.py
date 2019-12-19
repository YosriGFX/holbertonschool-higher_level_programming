#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        b = list(a_dictionary)[0]
        for a in a_dictionary:
            if a_dictionary[a] > a_dictionary[b]:
                b = a
        if b:
            return b
        else:
            return None
